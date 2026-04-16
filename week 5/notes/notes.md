# CS50P — Week 5: Unit Tests

## Overview

Week 5 introduces **unit testing**, a technique used to verify that individual parts of a program work correctly.

Instead of manually testing programs every time they change, developers write **automated tests** that validate their code.

This week focuses on:

- Writing testable functions
- Using Python’s `assert`
- Using the `pytest` testing framework
- Testing edge cases
- Structuring code for testing

---

# 1. What Are Unit Tests?

A **unit test** verifies that a **small piece of code (usually a function)** behaves as expected.

Example:

If you have a function:

```python
def square(n):
    return n * n
```

A unit test checks if it works correctly:

```python
assert square(2) == 4
```

If the function returns something incorrect, Python raises an error.

---

# 2. Why Unit Testing Is Important

Unit tests help developers:

- Detect bugs early
- Prevent regressions when modifying code
- Document expected behavior
- Build reliable software

Large software systems rely heavily on automated testing.

---

# 3. Writing Testable Code

Good programs separate logic into **functions**.

Bad example:

```python
x = int(input("x: "))
print(x * x)
```

This is difficult to test.

Better:

```python
def square(n):
    return n * n
```

Now the function can easily be tested.

---

# 4. Using `assert`

Python provides the `assert` statement to verify conditions.

Example:

```python
assert square(2) == 4
assert square(3) == 9
assert square(-2) == 4
```

If any test fails, Python raises:

```
AssertionError
```

---

# 5. Introducing pytest

The course uses **:contentReference[oaicite:1]{index=1}**, a powerful testing framework for Python.

Install it with:

```
pip install pytest
```

Run tests with:

```
pytest
```

---

# 6. Creating a Test File

Tests are usually placed in a separate file.

Example project:

```
calculator.py
test_calculator.py
```

The test file should start with **`test_`**.

---

# 7. Example Program

### calculator.py

```python
def square(n):
    return n * n
```

### test_calculator.py

```python
from calculator import square

def test_positive():
    assert square(2) == 4

def test_negative():
    assert square(-2) == 4

def test_zero():
    assert square(0) == 0
```

Running `pytest` will automatically detect and run the tests.

---

# 8. Running Tests

Command:

```
pytest
```

Example output:

```
3 passed in 0.02s
```

If a test fails:

```
FAILED test_calculator.py::test_positive
```

---

# 9. Testing Exceptions

Sometimes functions should raise errors.

Example function:

```python
def divide(x, y):
    return x / y
```

Test:

```python
import pytest
from calculator import divide

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

This verifies that the correct exception occurs.

---

# 10. Testing Edge Cases

Good tests include **edge cases**.

Examples:

- negative numbers
- zero
- empty strings
- very large numbers
- invalid inputs

Example:

```python
assert square(1000000) == 1000000000000
```

---

# 11. Testing Strings

Example function:

```python
def uppercase(text):
    return text.upper()
```

Tests:

```python
def test_uppercase():
    assert uppercase("hello") == "HELLO"
    assert uppercase("python") == "PYTHON"
```

---

# 12. Testing Invalid Input

Example function:

```python
def square(n):
    return n * n
```

Test for invalid input:

```python
import pytest
from calculator import square

def test_string_input():
    with pytest.raises(TypeError):
        square("hello")
```

---

# 13. Testing Multiple Cases

Example:

```python
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-3) == 9
```

---

# 14. Structuring Programs for Testing

Programs should separate:

- **logic**
- **input/output**

Example:

Bad:

```python
def main():
    x = int(input("x: "))
    print(x * x)
```

Better:

```python
def square(n):
    return n * n

def main():
    x = int(input("x: "))
    print(square(x))
```

Now `square()` can be tested independently.

---

# 15. Running Tests Automatically

Developers often run tests:

- before committing code
- before deploying applications
- during continuous integration (CI)

This ensures code changes do not break existing features.

---

# Key Concepts Learned in Week 5

By the end of Week 5 you should understand:

- What unit tests are
- Why testing is important
- How to write testable functions
- How to use `assert`
- How to install and use `pytest`
- How to test exceptions
- How to test edge cases
- How to structure code for testing

Unit testing helps developers write **more reliable and maintainable programs**.