# CS50P – Week 1: Conditionals

## Overview
Week 1 introduces **conditional statements** in Python.

Conditionals allow a program to **make decisions** by executing different code depending on whether a condition is `True` or `False`.

Programs become interactive by responding differently depending on user input.

---

# Boolean Values

Python has two Boolean values:

```
True
False
```

These values often result from **comparisons**.

Example:

```python
x = 5
print(x > 3)
```

Output:

```
True
```

---

# Comparison Operators

Comparison operators compare two values.

| Operator | Meaning |
|--------|--------|
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal |
| `<=` | less than or equal |
| `==` | equal |
| `!=` | not equal |

Example:

```python
x = 10
y = 20

print(x < y)
```

Output:

```
True
```

---

# if Statements

An `if` statement runs code **only if a condition is true**.

Syntax:

```python
if condition:
    code
```

Example:

```python
x = int(input("What's x? "))

if x > 0:
    print("x is positive")
```

---

# if / else

The `else` block runs if the `if` condition is **false**.

Syntax:

```python
if condition:
    code
else:
    code
```

Example:

```python
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# if / elif / else

Used when there are **multiple conditions**.

Syntax:

```python
if condition1:
    ...
elif condition2:
    ...
else:
    ...
```

Example:

```python
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

---

# Logical Operators

Logical operators combine conditions.

| Operator | Meaning |
|--------|--------|
| `and` | both conditions must be true |
| `or` | at least one condition must be true |
| `not` | reverses a condition |

Example:

```python
x = int(input("x: "))
y = int(input("y: "))

if x > 0 and y > 0:
    print("Both numbers are positive")
```

Example with `or`:

```python
if x == 0 or y == 0:
    print("One number is zero")
```

Example with `not`:

```python
if not x == 0:
    print("x is not zero")
```

---

# Nested Conditionals

Conditionals can exist **inside other conditionals**.

Example:

```python
x = int(input("x: "))

if x > 0:
    if x % 2 == 0:
        print("Positive even number")
```

---

# Simplifying Conditionals

Sometimes nested conditionals can be simplified.

Example:

```python
if x > 0:
    if x < 10:
        print("Single digit positive")
```

Better version:

```python
if 0 < x < 10:
    print("Single digit positive")
```

Python allows **chained comparisons**.

---

# String Comparisons

Strings can also be compared.

Example:

```python
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

---

# Case Sensitivity

String comparisons are **case-sensitive**.

```
Harry ≠ harry
```

To normalize user input:

```python
name = input("Name: ").lower()

if name == "harry":
    print("Gryffindor")
```

Useful string methods:

```
.lower()
.upper()
.strip()
.title()
```

---

# Membership Operator

Python allows checking if a value exists in a list using `in`.

Example:

```python
name = input("Name: ")

if name in ["Harry", "Hermione", "Ron"]:
    print("Gryffindor")
```

---

# Key Concepts from Week 1

By the end of Week 1 you should understand:

- Boolean values (`True`, `False`)
- Comparison operators
- `if`, `elif`, `else`
- Logical operators (`and`, `or`, `not`)
- Nested conditionals
- Simplifying conditions
- String comparisons
- Membership operator (`in`)

---

# Example Program

```python
name = input("Name: ").strip().title()

if name in ["Harry", "Hermione", "Ron"]:
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Unknown house")
```

---

# Summary

Week 1 focuses on **decision making in Python programs**.

Using conditional statements, programs can:

- evaluate conditions
- respond to user input
- execute different actions depending on results

This is a fundamental concept for building **interactive programs**.