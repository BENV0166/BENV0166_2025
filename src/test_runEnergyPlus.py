"""
Script to get around the Jupyter notebook issue of not printing output.

"""
from multiprocessing import Pool
from src.runEnergyPlus import run_energyPlus
import os
from pathlib import Path
import pandas as pd
import sys

ep_dir = sys.argv[1]
baseline_idf_path = sys.argv[2]
weather_file_path = sys.argv[3]
n_simulations = int(sys.argv[4])
print(n_simulations)

fileName = Path("outputs", "combinations", "combinations_Exercise_0.csv")

combinations = pd.read_csv(fileName, index_col = 0)

# The parameters for each iteration need to be put into a list of tuples to pass to the multiprocessing pool starmap function
# First convert the dataframe into a dictionary for each row of the dataframe
inputs = combinations.to_dict("records")
# Create the list of tuples 
# The ep_dir and idf_path and weather file path need to be part of the tuple as well as an integer i to mark the simulation number.
inputs = [(ep_dir, baseline_idf_path, weather_file_path, inputs[i], i) for i in range(n_simulations)]

# Run all of the simulations in parallel
# Set up multiprocessing by first obtaining the number of processors.
n_processors = os.cpu_count() 


if __name__ == "__main__":
    with Pool(processes = n_processors) as pool:
        print (f"Preparing to run {n_simulations} EnergyPlus simulation in parallel using {n_processors} processors")
        returnValues = pool.starmap(run_energyPlus, inputs)

print (f"\nFinished running all {n_simulations} simulations")
print (returnValues)