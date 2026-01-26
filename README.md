# python-improvers-2

Python Improvers course.  This is a new course based on lessons learned from the pre-pandemic Python Improvers course found at https://github.com/BritishGeologicalSurvey/python-improvers

The aim is to teach how to write Python scripts in a modular, reusable fashion using readable Pythonic code.

The lessons are provided as Jupyter notebooks in the [lessons](lessons) folder.
The code can be stepped through interactively and exercises can be done in-place.
Remember to save your copies to keep your changes.

The aim of the course is to show how people who are already familiar with Python for plotting
and scripting how to structure their code as a software developer would.
This makes it easier to read, test, reuse and share.
The [scripts](scripts) folder contains three different versions of a script for reading
text files and plotting the data within them.
By comparing them, we learn about functions, modules and classes and "Pythonic" code style.

## Local setup instructions

### Materials

Download this project repository, either via `git clone` or with "Download ZIP" within the "Code" menu.
Unzip it into a working directory e.g. `C:\Users\username\python-improvers-2`.

### Software

It is assumed that users are on Windows PCs, although the code should run in any operating system.
Ensure that the following software is installed on your machine:

+ `conda` or similar package manager (e.g. Anaconda/Miniconda)
+ VS Code
+ Git (optional)

Lesson 0 explains how to configure a Python virtual environment with the required packages.


### VS Code extensions

This course is aimed at VS Code, but can also be done with a combination of Spyder and Jupyter.
With appropriate extensions, VS Code can replicate the behaviour of both Spyder and Jupyter, but with better syntax highlighting and a built-in terminal.

The following VS Code extensions are recommended:

+ Python (Microsoft)
+ Pylance (Microsoft)
+ Jupyter (Microsoft)
+ Data Wrangler (Microsoft)
+ Flake8 (Microsoft)
+ Black Formatter (Microsoft)
+ Rainbow CSV (Mechatroner)
+ Vim (vscodevim) - only if you like Vim key bindings

Using VS Code more like Spyder.

+ Open Python file
+ At top right, press "Run Current File in Interactive Window".
+ Interactive window has Jupyter Variables button

To be able to execute code in the interactive terminal with `ctrl + enter`, do the following:

+ Preferences: Open User Settings
+ Search for "Jupyter execute selection"
+ Select the checkbox on "Jupyter > Interactive Window > Text Editor: Execute Selection".  This added `"jupyter.interactiveWindow.textEditor.executeSelection": true` to the settings.json.
