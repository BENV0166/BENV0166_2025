import os
from pathlib import Path
import subprocess
import time

from src.idf import modifyIDF
from src.processResults import processHourlyResults, processResilienceResults

def run_energyPlus (ep_dir, baseline_idf_path, weather_file_path, inputs, i):
    """
    This function modifies a baseline idf file usisng the modifyIDF function.

    This function creates a unique idf file by using the search and replace method.
    
    The simulation is then run in a temporary folder (iterations/iteration_{i})

    Returns a tuple of the returncode, and dictionaries of the hourly results, and thermal resilience results.

    """

    # Create the folder which the simulation will run in
    output_path = Path("iterations", f"iteration_{i}")
    Path.mkdir(output_path, exist_ok = True)

    # Create new path to save idf file based on iteration number
    new_idf_path = Path("iterations", f"iteration_{i}", f"iteration_{i}.idf")

    # Modify the idf file based on the inputs and save a new idf file
    modifyIDF (baseline_idf_path, new_idf_path, inputs)


    # Prepare the EnergyPlus command for Windows (NT) or Mac/Linux (Posix)
    if os.name == "nt": # Command for Windows users
        ep_path = Path (ep_dir, "energyplus.exe")
        ep_cmd = f'"{ep_path}" {new_idf_path} -w {weather_file_path} -d {output_path}'

    elif os.name == "posix": # Generate command for Mac/Linux Users
        ep_path = Path (ep_dir, "energyplus")
        ep_cmd = f"/{ep_path} {new_idf_path} -w {weather_file_path} -d {output_path}"


    # Run the simulation through a command line call.
    print (f"Beginning EnergyPlus simulation of iteration {i}.", flush = True)
    t0 = time.time()
    retcode = subprocess.run(ep_cmd, shell = True, stdout = subprocess.DEVNULL, stderr=subprocess.STDOUT) 
    t1 = time.time()

    if retcode.returncode == 0:
        print (f"Finished EnergyPlus simulation of iteration {i}. Time of simulation = {t1 - t0:.4f} s.", flush = True)
        # Analyse the results
        hourlyResults = processHourlyResults(Path("iterations", f"iteration_{i}", "eplusout.csv"))
        resilienceResults = processResilienceResults(Path("iterations", f"iteration_{i}", "eplustbl.csv"))

    else:
        print (f"Error in EnergyPlus simulation of iteration {i}", flush = True)
        # Return dummy results
        hourlyResults = None
        resilienceResults = None

    return retcode, hourlyResults, resilienceResults