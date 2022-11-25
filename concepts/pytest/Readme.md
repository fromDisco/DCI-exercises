# PyTest
# Run pytest
- run pytest in discovery mode
```console
pytest
```
- run only specific function in a module
```console
pytest test_file.py::test_func_val_error
```
- run only specif method of a TestClass in a module
```console
pytest test_file.py::TestClass::test_func_val_error
```


## Discovery Mode
- if no arguments are passed discovery mode starts from actual path recurses into directories until *norecursdirs*
- in theses directories search for *test_\*.py*, *\*_test.py*
```console
python3 -m pytest
```
- from the found files collect test items
    + *test* prefixed functions outside of class
    + *test* prefixed functions or methods inside *Test* prefixed classes (without \_\_init\_\_)
    + unittest.TestCase subclassing methods