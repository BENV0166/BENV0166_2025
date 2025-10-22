The following are steps that I use to set up environments and install packages using VS Code. The first is the method virtual environment method which is what I use and prefer, the second is the method to use if want to use a conda environment.

If you are having trouble getting notebooks to run because of packaging issues, try running these steps

## Virtual Environment
1. Create a virtual environment by following the menus:
    * Ctrl+Shift+P > Python: Create Environment > Venv > Python 3.12.x > requirements.txt
        * The requirements.txt is a list of all packages including version numbers needed for this module.
        * It may take a few minutes to download all packages
        * You should see a .venv folder in your file explorer on the left
        * Alternatively, you can use the command pip install -r requirements.txt --target=.venv
        * Ensure that .conda is the selected kernel
2. If you need to install another package
    * Open up a terminal at the bottom of the workspace and type the following:
        * pip install {*packageName*} --target=.venv
        * The --target=.venv ensures the packages get installed in the virtual environment and not the base Python version.

## Conda Environment
1. Create a conda environment by following the menus
    * Ctrl+Shift+P > Python: Create Environment > Conda > Prefix > Python 3.12.x 
    * You should see a .conda folder in your explorer on the left
    * Ensure that .conda is the selected kernel
2. Now you need to install the packages
    * Option 1: In the terminal type pip install -r requirements.txt --target=.conda
    * Option 2: Manually install packages using conda install {*packageName*}. 

## Packages Used
The full list of packages used in this module (subject to change)

* ipykernel
* numpy
* pandas
* matplotlib
* matplotlib-inline
* scipy
* scikit-optimize (type in pip install skopt)
* scikit-learn
* paretoset
* pymoo
