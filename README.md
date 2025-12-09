# python-improvers-2

Python Improvers course.  This is a new course based on lessons learned from the pre-pandemic Python Improvers course found at https://github.com/BritishGeologicalSurvey/python-improvers

The aim is to teach how to write Python scripts in a modular, reusable fashion using readable Pythonic code.


## Local setup instructions

Ensure that the following software is installed on your machine:

+ `conda` or similar package manager (e.g. Anaconda/Miniconda)
+ VS Code
+ Git (optional)

Download the project repository, either via `git clone` or with "Download ZIP" within the "Code" menu.

Open a terminal window that has access to the `conda` command.
On Windows, this may be by choosing the CMD.exe prompt from the Anaconda Navigator.

Create the virtual environment.

```bash
conda env create -f environment.yml
```

If you are not on a Windows system, or have problems installing the packages, try using `environment_unversioned.yml` instead.
This doesn't have pinned versions, which will allow the solver to choose appropriate versions for your system.


## IDEs

This course is aimed at VS Code, but can also be done with a combination of Spyder and Jupyter.
With appropriate extensions, VS Code can replicate the behaviour of both Spyder and Jupyter, but with better syntax highlighting and a built-in terminal.

The following VS Code extensions are recommended:

+ Python (Microsoft)
+ Pylance (Microsoft)
+ Jupyter (Microsoft)
+ Data Wrangler (Microsoft)
+ Flake8 (Microsoft)
+ Black Formatter (Microsoft)
+ RainbowCSV (Mechatroner)
+ Vim (vscodevim) - only if you like Vim key bindings

Using VS Code more like Spyder.

+ Open Python file
+ At top right, press "Run Current File in Interactive Window".
+ Interactive window has Jupyter Variables button

To be able to execute code in the interactive terminal with `ctrl + enter`, do the following:

+ Preferences: Open User Settings
+ Search for "Jupyter execute selection"
+ Select the checkbox on "Jupyter > Interactive Window > Text Editor: Execute Selection".  This added `"jupyter.interactiveWindow.textEditor.executeSelection": true` to the settings.json.

### Linting

The following command-line linting tools are recommended.
These are provided in the environment specification.

```python
flake8 test.py  # General code layout, redundant code and syntax errors
pylint test.py  # Code style
mypy test.py  # Static type checking
```

## Lessons

The lessons are provided as IPython notebooks in the [lessons](lessons) folder.
As well as the main lessons, topics that have been covered in Python clinics can also be included.
Some of these are:

+ Dates and times with datetime
+ Text parsing and regular expressions
+ Testing code with pytest
+ Geopandas for spatial data analysis
+ Running external commands with subprocess
+ Interactive debugging with breakpoint and pdb
