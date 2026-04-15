# CS50P — Week 3: Exceptions

## Overview

Week 3 focuses on **exceptions**, which are errors that occur during the execution of a program.

Instead of letting a program crash when an error occurs, Python allows programmers to **handle errors gracefully** using exception handling.

This week teaches how to:

- Detect errors
- Prevent programs from crashing
- Validate user input
- Write more robust programs

---

# 1. What is an Exception?

An **exception** is an error that occurs while a program is running.

Example:

```python
x = int(input("What's x? "))
print(x)
```

If the user types:

```
hello
```

Python produces an error:

```
ValueError: invalid literal for int()
```

This happens because `"hello"` cannot be converted to an integer.

---

# 2. The `try` and `except` Blocks

Python allows us to **catch errors** using `try` and `except`.

## Syntax

```python
try:
    code that might cause an error
except:
    code that runs if an error occurs
```

### Example

```python
try:
    x = int(input("What's x? "))
    print(x)
except ValueError:
    print("That is not a number.")
```

Now if the user types something invalid, the program will not crash.

---

# 3. Handling Specific Exceptions

It is best practice to catch **specific exceptions**, not all errors.

Example:

```python
try:
    x = int(input("What's x? "))
    print(x)
except ValueError:
    print("Invalid input")
```

This only catches `ValueError`.

Other types of errors will still be visible, which helps debugging.

---

# 4. Avoid Using Bare `except`

This is considered **bad practice**:

```python
try:
    x = int(input("What's x? "))
except:
    print("Error")
```

Why?

Because it hides **all errors**, including unexpected bugs.

Always prefer:

```python
except ValueError:
```

---

# 5. Using `else`

The `else` block runs **only if no exception occurs**.

Example:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("Invalid input")
else:
    print(f"x is {x}")
```

Flow:

1. Try to convert input
2. If error → run `except`
3. If no error → run `else`

---

# 6. Using `pass`

Sometimes we want to **ignore an error and continue execution**.

Example:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    pass

print("Done")
```

If an error occurs, Python simply **skips the exception and continues**.

---

# 7. Looping Until Valid Input

Exceptions are often used with loops to **keep asking the user until valid input is provided**.

Example:

```python
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("Please enter a number.")
```

This loop continues until the user enters a valid number.

---

# 8. Creating a Function for Input Validation

We can place validation logic inside functions.

Example:

```python
def get_int():
    while True:
        try:
            return int(input("Integer: "))
        except ValueError:
            pass
```

Usage:

```python
x = get_int()
print(f"x is {x}")
```

This function **guarantees that the returned value is an integer**.

---

# 9. Raising Exceptions

Python allows programmers to **manually raise exceptions**.

Example:

```python
raise ValueError
```

Example with validation:

```python
def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
```

This signals that the function received an invalid argument.

---

# 10. Multiple Exceptions

A `try` block can handle multiple types of exceptions.

Example:

```python
try:
    x = int(input("x: "))
    y = int(input("y: "))
    result = x / y
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Possible errors handled:

- invalid number input
- division by zero

---

# 11. Real-World Use Case

Exceptions are commonly used when:

- validating user input
- reading files
- working with APIs
- handling network requests
- performing mathematical operations

Example with file reading:

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File does not exist.")
```

---

# 12. Good Exception Handling Practices

Best practices:

- Catch **specific exceptions**
- Avoid hiding errors
- Use exceptions to validate user input
- Keep `try` blocks small and focused
- Use loops to retry operations when needed

---

# Key Concepts Learned in Week 3

By the end of Week 3 you should understand:

- What exceptions are
- How to use `try`
- How to use `except`
- How to use `else`
- How to use `pass`
- How to validate user input safely
- How to raise exceptions
- How to handle multiple types of errors

These concepts help create **robust and reliable Python programs** that do not crash when unexpected input occurs.