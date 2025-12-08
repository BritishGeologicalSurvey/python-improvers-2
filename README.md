# python-improvers-2

Python Improvers course.  This is a new course based on lessons learned from the pre-pandemic Python Improvers course found at https://github.com/BritishGeologicalSurvey/python-improvers

The aim is to teach how to write Python scripts in a modular, reusable fashion using readable Pythonic code.

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

The following linting tools are recommended.

```python
flake8 test.py
pylint test.py
mypy test.py  # Needs mypy --install-types to help
```