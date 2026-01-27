### Differences between good and bad

+ functions
+ imports at top
+ functions have docstrings
+ __name__ == "__main__"
+ good uses logger - run Good again with logging.DEBUG to see the difference
+ good uses type hints ( link to RealPython type hints )

+ bad has no return value from function (but type says that it is a string)
+ bad has no separation between function and other code
+ bad could leave file open if functions errors
+ bad defines `f` outside the function


Flake8

mypy

+ demonstrate type hints in existing scripts
+ demonstrate autocomplete with dot notation
+ Settings > Pylance > type checking
+ demonstrate spotting issues with return type
