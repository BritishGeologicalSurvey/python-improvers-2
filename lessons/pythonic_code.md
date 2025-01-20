---
title: "Writing Pythonic code"
teaching: 50
exercises: 40
questions:
- "How do I write code in a Pythonic style?"
objectives:
- "Learn Pythonic idioms for writing clean, concise code"
keypoints:
- "Tuple unpacking avoids referring to data by their list index"
- "List comprehensions are a concise way to loop over data"
- "Context managers tidy up open files or connections"

---

## What is 'Pythonic' code?

Pythonic code uses Python's style conventions and idioms in a way that expresses the programmer's intent in an easily readable and understandable way.
This lesson covers both the style conventions and the idioms.

In addition, Pythonic code makes use of features from Python's [Standard Library](https://docs.python.org/3/tutorial/stdlib.html) to handle common
problems e.g.

+ [`os`](https://realpython.com/working-with-files-in-python/) and [`pathlib`](https://realpython.com/python-pathlib/) modules for navigating the file system
+ [`datetime`](https://pymotw.com/2/datetime/) module for handling dates and times
+ [`re`](https://pymotw.com/3/re/) module for text processing with regular expressions
+ [`csv`](https://realpython.com/python-csv/) module for handling comma separated data

Each of the module names above links to a tutorial that gives much more detail
than we can in this lesson.  It is recommended that you read them all in your
own time.

Pythonic style comes with experience - the more code that you are exposed to,
the faster you will learn.
Reading tutorials and books, or watching talks from Python conferences on YouTube is a good way to see how code is written.
It is also valuable to learn from others by letting them review your code, or
by reviewing theirs.

## Pythonic idioms

### Introduction

The Python language was designed to be readable.  It doesn't enforce types or the use of classes, or use brackets or semi-colons to break up sections of code.
It has many idioms that can be used to write instructions with fewer lines of
code than would be required in other langages.

The following text is copied from [What is Pythonic?](https://blog.startifact.com/posts/older/what-is-pythonic.html)

> Idioms are frequently not straightforwardly portable from another programming language. For example, the idiomatic way to perform an operation on all items in a list in C looks like this:
>
> ~~~ c
> for (i=0; i < mylist_length; i++) {
>     do_something(mylist[i]);
> }
> ~~~
>
> The direct equivalent in Python would be this:
>
> ~~~ python
> i = 0
> while i < mylist_length:
>     do_something(mylist[i])
>     i += 1
> ~~~
>
> That, however, while it works, is not considered Pythonic. It's not an idiom the Python language encourages. We could improve it. A typical idiom in Python to generate all numbers in a list would be to use something like the built-in range() function:
>
> ~~~ python
> for i in range(mylist_length):
>     do_something(mylist[i])
> ~~~
>
> This is however not Pythonic either. Here is the Pythonic way, encouraged by the language itself:
>
> ~~~ python
> for element in mylist:
>     do_something(element)
> ~~~

The following sections highlight some common Python idioms.  Use these to write
Pythonic code.


### Empty containers and None are _Falsy_

The code below will only run if data contains a value:

```python
if data is not None:
    do_something()
```

The equivalent for a list may be:

```python
if len(data) > 0:
    do_something()
```

The following values are considered `False` in Python:

`None`, 0, 0.0, `''`, `[]`, `()`, `{}`

Therefore, both cases above can be written as:

```python
if data:
    do_something()
```

(But beware of cases where 0 is a valid value that means something different to
`None`.)

### Python functions are objects

Python functions are true objects.
To see this, use Python's `dir` function to list the attributes that they have:

```python
dir(min)
```
This means that they can be stored in lists or dictionaries like any other
object.
Python has built-in functions for working on collections of data.

```python
data = (2, 0, 3)
for current_function in [min, max, sum, any, all, len, sorted]:
    print(f"{current_function.__name__}({data}) --> {current_function(data)}")
```

Other useful functions are found in the `math` library.

```python
from math import floor, ceil, sin, cos, tan, log, pi

for current_function in [floor, ceil, sin, cos, tan, log]:
    print(f"{current_function.__name__}(pi) --> {current_function(pi)}")
```


### Tuple unpacking

Tuple upacking assigns the elements of a tuple (or other iterable) to
individual variables in a single line.
It is especially useful when processing rows of data returned from a database
or CSV file.
It can lead to more easily understandable code.

Accessing attributes by position:

```python
result = ('AB654', datetime(2010, 4, 14), 5.21, 7.4, 6.02)

mean = (result[2] + result[3] + result[4]) / 3.0
text_summary = f'{result[0]}: {mean} (Analysed {result[1].date().isoformat()})'
print(text_summary)
```

With tuple unpacking:

```python
result = ('AB654', datetime(2010, 4, 14), 5.21, 7.4, 6.02)

sample, analysed, run1, run2, run3 = result
mean = (run1 + run2 + run3) / 3.0
text_summary = f'{sample}: {mean} (Analysed {analysed.date().isoformat()})'
print(text_summary)
```

Python's
[namedtuple](https://dbader.org/blog/writing-clean-python-with-namedtuples)
feature is useful when using lots of data of this form.
It provides access to data at `result.sample`, `result.run1` etc.


### List comprehensions

List comprehensions are a concise syntax for operations that would usually be
done via loops.
The following is an example:

```python
from math import pi
radii = [1.23, 2.34, 3.45, 4.56]

areas = []
for radius in radii:
    areas.append(pi * radius**2)
```

The list comprehension version is:

```python
areas = [pi * radius**2 for radius in radii]
```

Note that for numerical computing, `numpy` arrays are more efficient:

```python
import numpy as np

radii = np.array([1.23, 2.34, 3.45, 4.56])
areas = np.pi * radii**2
```

List comprehensions can use `if` statements to act as a filter:

```python
results = {'AB234': 0.78, 'AB432': 0.65, 'AB112': 0.3}
passes = [code
          for code, score in results.items()
          if score > 0.5]
```

[Generator expressions](https://dbader.org/blog/python-generator-expressions), denoted by `()` can be used to create sequences where you wouldn't want to evaluate a whole list into memory.
Python also has [dictionary comprehensions](https://www.programiz.com/python-programming/dictionary-comprehension), denoted by `{}` to create
dictionaries.

### Exercise

Apply tuple unpacking and list comprehensions to `earthquake_magnitudes_1.py`.
### Replacing elif with dictionaries

The following function is a currency converter:

```python
def convert_currency(pounds, target='euros'):
    """
    Convert the given amount in Pounds Sterling into the target currency.
    """
    # Convert to lower case
    target = target.lower()

    # Get exchange rate
    if target == 'euros':
        exchange_rate = 1.12
    elif target == 'dollars':
        exchange_rate = 1.26
    elif target == 'krona':
        exchange_rate = 167.25
    else:
        raise(ValueError(f"Currency not supported: {target}, choose from "
                          "Euro, Dollars, Yen)

    return pounds * exchange_rate
```

It can be tested with:

```python
pounds = 2.00
assert convert_currency(pounds, target='euros') == 2.24
assert convert_currency(pounds, target='dollars') == 2.52
assert convert_currency(pounds, target='krona') == 334.5
```

Python dictionaries can provide a "mapping" between pairs of values.
It is common for the keys to be strings, but they could be integers or any
other non-mutable (hashable) item.
As functions and classes are objects in Python, these can keys or values.
Lists, dictionaries or sets are mutable and cannot be keys.

Using a dictionary mapping can replace verbose `elif` clauses.

```python
def convert_currency(pounds, target='euros'):
    """
    Convert the given amount in Pounds Sterling into the target currency.
    """
    exchange_rates = {'euros': 1.12,
                      'dollars': 1.26,
                      'krona': 167.25}
    
    try:
        exchange_rate = exchange_rates[target.lower()]
    except:
        raise(ValueError(f"Currency not supported: {target}, choose from "
                         f"{exchange_rates.keys()}"))

    return pounds * exchange_rate
```

Note the exception for an unrecognised key.  Dictionaries also have a `.get()`
method that can return a default value if an unrecognised key is provided.
Also note that the list of valid currencies is now generated dynamically.


### Context managers


Context managers provide a way to automatically manage resources while running
a section of code.
They are commonly used with files and network connections e.g. to databases.

Consider the following code that processes all the lines in a text file:

```python
f = open('my_file.txt')

for line in f.readlines():
    do_something(line)

f.close()
```

If `do_something(line)` raises an exception then `f.close()` will not be called
and the file will be left open.
This situation can be avoided as follows:

```python
f = open('my_file.txt')

try:
    for line in f.readlines():
        do_something(line)
finally:
    f.close()
```

The `finally` block is always called, even if the `try` block raises an
exception.
However a more Pythonic way is to use the `with` command to open a context
manager:

```python
with open('my_file.txt') as f:
    for line in f.readlines():
        do_something(line)
```

Using `open` as a context manager ensures that the file is closed in all
situations.
If you find yourself using `try`, `finally` pattern in your code, the
Standard Library's [contextlib](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) module contains tools for defining your own
context managers.


### Exercise

+ Apply a dictionary mapping to the `classify_magnitude` function in `earthquake_magnitudes_1.py`.
+ Use a context manager for output file writing in `earthquake_magnitudes_1.py`.

One of the useful `math` functions defined above can calculate the category key for
a given magnitude value.


#### Bonus exercise

Replace the rows in `data` with a `namedtuple` called `Earthquake` and update
the rest of the code to use named attributes.