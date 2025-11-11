import os
from pathlib import Path
import subprocess
import time

from src.processResults import processHourlyResults, processResilienceResults

def run_energyPlus_6A(ep_dir, baseline_idf_path, weather_file_path, value, i):
    """
    This function prepares the idf file 1-storey_Example6A.idf by modifying the wall insulation thickness value only.
    
    This function creates a unique idf file by using the search and replace method.
    
    The simulation is then run in a temporary folder (iterations/iteration_{i})

    Returns a tuple of the returncode, and dictionaries of the hourly results, and thermal resilience results.

    """

    # Open the idf as a text file.
    with open (baseline_idf_path, "r") as f:
        contents = f.read()

    # Execute the search and replace method.
    key = "@wallInsulationThickness@"
    contents = contents.replace(key, str(value))

    # Create the folder which the simulation will run in
    output_path = Path("iterations", f"iteration_{i}")
    Path.mkdir(output_path, exist_ok = True)

    # Write the updated idf file to the new_idf_path where it can then be run.
    new_idf_path = Path("iterations", f"iteration_{i}", f"iteration_{i}.idf")
    with open(new_idf_path, "w") as f:
        f.write(contents)

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
    retcode = subprocess.run(ep_cmd, shell = True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) 
    t1 = time.time()


    # If EnergyPlus has a return code of 0, the simulation completed successfully
    # Otherwise an error occurred and this will be flagged.
    # If the simulation has successfully completed we will also collect the results

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