---
title: "Functions and arguments"
teaching: 40
exercises: 20
questions:
- "Why should I use functions in my code?"
- "What does `if __name__ == '__main__':` do?"
- "How can I turn a script into a command-line tool?"
objectives:
- "Learn how to structure code using functions"
keypoints:
- "Functions divide code into reusable and testable chunks"
- "`if __name__ == '__main__'` prevents scripts being run when imported as
  modules"

---

## Breaking code into functions

Functions allow code to be reused and help programmers follow the *Don't
Repeat Yourself* (DRY) principle.
They can take inputs (called _parameters_) and perform the same operations
on different values.
Using the `import` command, functions defined in one module can be used in
many other scripts.

Functions can also be used to break code into logical chunks.
Each function should *do one thing*.
Such functions are easier to test than a large program.
As they have a local scope, they are protected from changes to variables
elsewhere in the code.
If they have descriptive names, the code becomes self-documenting and needs
fewer comments.

Functions can can be defined in any order and can call other functions.
Thus, the main structure of the program to be written at the top
of the file, before the definition of the functions that it calls.
By convention, this is often called the `main()` method.
The `main()` method provides a high-level summary of how the script works that is easy to
find, like the abstract of a scientific paper.

Below is an example structure of a simple data analysis script.


```python
# process_instrument_data.py

CALIBRATION_COEFF = 1.2345

def process_instrument_data_file(input_file, output_file):
    """
    This is the main method of the module and calls other functions defined below.
    It isn't called `main()` this time, because we expect to import it into other
    code, so it is useful to have a descriptive name.
    """
    raw_data = read_instrument_data(input_file)
    result = process_raw_data(raw_data)
    save_output(result, output_file)


def read_instrument_data(input_file):
    """Read file and extract data."""
    print(f"Reading {input_file}")
    # <insert code here...>
    return (1, 2, 3)


def process_raw_data(data):
    """
    Process data from the instrument (this uses the global calibration
    coefficient.
    """
    print(f"Processing {data}")
    # <insert code here...>
    intermediate_result = _do_some_tricky_processing_step(data)
    return (4, 5, 6)


def _do_some_tricky_processing_step(data):
    """
    Some logically self-contained processing step within the main processing.
    The underscore at the start of the name says this is a "hidden"
    function.  This means that it is only meant for internal use and we wouldn't
    expect other users to import and call it by itself.
    """
    print(f"Intermediate processing step on {data}")
    # <insert code here...>
    return (2, 3, 4)


def save_output(result, output_file, format='png'):
    """
    Save output.  The `format` parameter is optional and has a default
    value of 'png'
    """
    print(f"Saving {result} to {output_file} in {format} format")
    # <insert code here>
    return


# Call the processing function
process_instrument_data_file('my_input_file.txt', 'my_output_file.txt')
```

### Exercise

Examine the file `earthquake_magnitudes_2.py` in the `code` directory.
It is a PEP 8 compliant and Pythonic version of the code we checked earlier.
The different sections can be modified to turn them into functions.
Use the code comments to choose the function name and think about what the
inputs and outputs would be.

For example:

```python
# Find largest earthquake
largest = max(row[4] for row in data)
```

becomes:

```python
def find_largest_earthquake(data)
    largest = max(row[4] for row in data)
    return largest 
```

+ Refactor the file to turn the code sections into functions.
+ Create a `main()` function at the top of the file that runs them in order,
  passing appropriate data between them.
+ Call the `main()` function at the end of the file to run your script.

Remember that the file should still run and produce exactly the same output.


## if \_\_name\_\_ == '\_\_main\_\_'

When a Python file is imported as a module, all lines within it are read and
non-indented code blocks are executed.

Importing `process_instrument_data.py` from above will run the script.
We don't want this if we are trying to import some of the data or functions.

```python
from process_instrument_data import process_raw_data, CALIBRATION_COEFF
```

> Note: the code is only executed on first import. To reimport a module, it
> may be necessary to restart IPython kernel or use
> [importlib.reload()](https://docs.python.org/3/library/importlib.html#importlib.reload).

Adding an `if __name__ == '__main__'` block to the code avoids this.  The
indented block will only be executed when the Python file has been called as a
script.

```python
if __name__ == '__main__':
    process_instrument_data_file('my_input_file.txt', 'my_output_file.txt')
```

`__name__` is a special Python variable that refers to the name of the module
the code is being imported from.  When a file is run as a script, its code has
not been imported so the value is set to `__main__`.

This can be seen by adding `print(f"Hi, my __name__ is '{__name__}')"` to the
`process_instrument_data.py` code and running or importing it.


### Exercise

+ Add an `if __name__ == '__main__':` block to your modified version of
  `earthquake_magnitudes_1.py`

Remember that the file should still run and produce exactly the same output.