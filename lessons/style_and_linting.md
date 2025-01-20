---
title: "Writing Pythonic code"
teaching: 50
exercises: 40
questions:
- "How do I write code in a Pythonic style?"
objectives:
- "Learn how to apply PEP 8 coding conventions to code"
- "Learn Pythonic idioms for writing clean, concise code"
keypoints:
- "Use PEP 8 conventions to style your code in an easily readable way"
- "Development environments and _flake8_ check your code for you"
- "Tuple unpacking avoids referring to data by their list index"
- "List comprehensions are a concise way to loop over data"
- "Context managers tidy up open files or connections"

---

## The Style Guide for Python Code: PEP8

### Introduction

The coding conventions for Python code are written down in [PEP 8 -- Style
Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).
PEP8 covers indentation, line lengths, use of whitespace, comments, naming
conventions.
Following PEP 8 makes your code easier to read and more readily understood by
other developers.

Example PEP 8 conventions are:

+ Variables and functions are written in `snake_case`
+ Class names are written in `CamelCase`
+ Indent code blocks using 4 spaces
+ Use a space around operators e.g. `1 + 1` and after commas e.g. `(1, 2, 3)` 

The Real Python [How to Write Beautiful Python Code with PEP 8](https://realpython.com/python-pep8/) tutorial gives a nice overview.

### Checking your code

There are many tools for checking if your code conforms to PEP 8 standards.
Development environments e.g. Spyder, PyCharm highlight errors.

The command line tool `flake8` can be used to check code, too:

```bash
flake8 path/to/my/files
```

The `pylint` tool checks PEP 8 as well as highlighting other problems in your
code.

In Visual Studio Code, open the Command Palette ("Ctrl + Shift + P") and use "Select Linter" and "Run Linting" commands to analyse your code.
In Spyder, pressing "Source > Run static code analysis (F8)" will produce
a report on your code quality using `flake8` and `pylint`.

### Exercise

Download an unzip the [Earthquake code and data]({{page.root}}/files/earthquake_code.zip) file.
Examine the file `earthquake_magnitudes_0.py`.
Run it to see what it does.
The code contains many style errors.
Use `flake8` and `pylint` to identify them and then fix them.

It is possible to configure exceptions to rules for individual linters (see [.flake8](.flake8) file).
Ignore the "Constant name doesn't conform to UPPER_CASE naming style" from Pylint.
This error appears because Pylint isn't expecting simple script files.

The code has been written to demonstrate many Python features and opportunities for improvement.
It "real life", this type of analysis is well suited to the [GeoPandas](https://nbviewer.jupyter.org/github/BritishGeologicalSurvey/geopandas-demo/blob/master/GeoPandas_demo.ipynb) module.