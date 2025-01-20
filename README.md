# python-improvers-2
Python Improvers course.  This is a new course based on lessons learned from the pre-pandemic Python Improvers course found at https://github.com/BritishGeologicalSurvey/python-improvers

## IDE

Making VS Code more like Spyder.

+ Install Jupyter extension from Microsoft (and Data Wrangler to view dataframes)
+ Open Python file
+ At top right, press "Run Current File in Interactive Window".
+ Interactive window has Jupyter Variables button

For more IPython-like behaviour, I also needed to go to:

+ Preferences: Open User Settings
+ Search for "Jupyter execute selection"
+ Select the checkbox on "Jupyter > Interactive Window > Text Editor: Execute Selection".  This added `"jupyter.interactiveWindow.textEditor.executeSelection": true` to the settings.json.

The "Rainbow CSV" extension is also useful.

### Linting

```python
flake8 test.py
pylint test.py
mypy test.py  # Needs mypy --install-types to help
```