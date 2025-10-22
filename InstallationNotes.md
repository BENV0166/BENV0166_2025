## Python
Requirements: Minimum Python 3.12 (though earlier versions should still work)

We will be using Python notebooks throughout the course for weekly exercises and as the foundation for Coursework 2. I will be running Jupyter Notebooks in Visual Studio Code throughout the course. You may use other programs (such as JupyterLab, Google Collab) if you prefer, but be advised some features such as Git, may not work as seamlessly as in VS Code.

* For instructions on how to install VS Code, visit here [link](https://code.visualstudio.com/download) and check out this tutorial [link](https://code.visualstudio.com/docs/getstarted/getting-started)
* For instructions on how to install the Python extension for VS Code and get started, visit here [link](https://code.visualstudio.com/docs/python/python-tutorial)
* For instructions on how to install the Jupyter extension for VS Code and get started, visit here [link](https://code.visualstudio.com/docs/datascience/jupyter-notebooks?originUrl=%2Fdocs%2Fpython%2Fpython-tutorial)

We will be using a number of Python data science packages such as numpy, pandas, matplotlib, scikit etc. You choose to install these through Anaconda virtual environment, or install the necessary files using pip install and the provided requirements.txt in the Github repository. For more info on environments and installing packages visit here [link](https://code.visualstudio.com/docs/python/environments?from=20423)

## Git

Git is a version control manager which enables users to develop and share their code collaboratively through repositories. We will be using the hosting service Github to distribute files throughout the term.

### Installing Git

* Go to the Git Downloads Website [link](https://git-scm.com/downloads)
    * You can also access this through VS Code by selecting the Source control icon (the one with three circles) and Press the *Download Git for Windows* button 
* Select your operating system and follow the instruction to download and install Git
    * Don't change any of the recommended options in the installation wizard

### Cloning a Repository

#### VS Code Instructions

* Click on Clone Git Repository on the VS Code Home Screen
* Select the repository to be cloned
    * Enter the repository's URL in the search bar
    * Only available if you have access to the repository
* Select where you want to save the repository
* Open the folder in VS Code

#### Using Git GUI

* Right click on a folder you wish to import the github repository into
* Select  *Git GUI here* and a new window should pop up
* Select *Clone Existing Repository*
* Enter the URL of the repository in the Source Location box
* Enter the name of the Target Directory you wish to save the files into
* Go to windows explorer and confirm that the files are there. A folder named *.git* should also be there (may need to enable *show hidden files*)

#### Using Git Bash Terminal

* Right click on a folder you wish to import the github repository into
* Select  *Git Bash here* and a new terminal should pop up
* Type the following into the terminal
    * git clone {*URL of the repository*}.git
    * NOTE: Do not enter the braces and remember to include the extension
* A GitHub sign-in request may pop-up. Enter your credentials.
* Go to windows explorer and confirm that the files are there. A folder named *.git* should also be there (may need to enable *show hidden files*)

### Pulling from a Repository

* It is good practice to *pull* any changes which have been made to a repository before any session
    * I will be adding items week-by-week throughout the term

#### VS Code
* In VS Code, select the Source Control icon on the left toolbar. 
    * Under the changes tab, select pull.

#### Git GUI
This is not as convenient as it is in VS Code
* Select Remote -> Fetch From -> [Branch]
* Then, Select Merge -> Local Merge

#### Git Bash Terminal
* git pull {*branchName optional*}

## EnergyPlus
EnergyPlus is a dynamic energy modelling software engine which is widely used in academics and industry.It is considered one of the state-of-the-art tools of the industry and we will be using to perform simulations throughout the module.

### Installing EnergyPlus

* Download EnergyPlus v25.1 form the website. [link](https://energyplus.net/downloads)
    * Note the directory that you have saved it to
* Open the EnergyPlus folder and you should see two executable files
    * EP-launch.exe which is a UI for running simulation files
    * energyplus.exe which is the simulation engine. We will call this executable in the Python script.

### Running EnergyPlus
* You can run an EnergyPlus simulation through the EP-launch GUI by selecting one of the sample files and weather files provided in the installation.
* You can also have a look at the idf editor and results file.
* **NOTE** We won't be using the EnergyPlus UI in the module. We will learn how to run and modify EnergyPlus simulations through Python.
