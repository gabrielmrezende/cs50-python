# CS50P — Week 2: Loops

## Overview

Week 2 of CS50’s Introduction to Programming with Python focuses on **loops**, which allow programs to repeat actions multiple times. Loops are fundamental for automating repetitive tasks and processing data efficiently.

Python provides two main looping structures:

- `while`
- `for`

Understanding loops is essential for building real programs and solving computational problems.

---

# 1. The `while` Loop

A `while` loop repeats code **as long as a condition is true**.

## Syntax

```python
while condition:
    code
```

### Example

```python
i = 0

while i < 3:
    print("meow")
    i += 1
```

Output:

```
meow
meow
meow
```

### Explanation

1. The variable `i` starts at `0`.
2. The loop runs while `i < 3`.
3. Each iteration increases `i` by 1.
4. When `i` becomes `3`, the loop stops.

---

# 2. Infinite Loops

An infinite loop occurs when the condition **never becomes false**.

Example:

```python
while True:
    print("Hello")
```

This loop runs forever.

To stop it manually in the terminal:

```
CTRL + C
```

---

# 3. The `break` Statement

`break` immediately stops a loop.

Example:

```python
while True:
    n = int(input("Number: "))
    if n > 0:
        break
```

The program continues asking until the user enters a positive number.

---

# 4. The `continue` Statement

`continue` skips the rest of the current iteration and starts the next loop iteration.

Example:

```python
while True:
    n = int(input("Number: "))
    if n < 0:
        continue
    else:
        break
```

If the number is negative, the loop restarts immediately.

---

# 5. The `for` Loop

A `for` loop repeats code a **specific number of times** or iterates through a sequence.

## Syntax

```python
for variable in sequence:
    code
```

### Example

```python
for i in range(3):
    print("meow")
```

Output:

```
meow
meow
meow
```

---

# 6. The `range()` Function

`range()` generates a sequence of numbers.

### Example

```python
range(3)
```

This produces:

```
0, 1, 2
```

Example with printing:

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

# 7. Iterating Over Lists

A `for` loop can iterate over elements in a list.

Example:

```python
students = ["Harry", "Ron", "Hermione"]

for student in students:
    print(student)
```

Output:

```
Harry
Ron
Hermione
```

---

# 8. Iterating with Indexes

To access both the index and value:

```python
students = ["Harry", "Ron", "Hermione"]

for i in range(len(students)):
    print(i, students[i])
```

Output:

```
0 Harry
1 Ron
2 Hermione
```

---

# 9. Iterating Over Dictionaries

Dictionaries store key-value pairs.

Example:

```python
students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student])
```

Output:

```
Harry Gryffindor
Hermione Gryffindor
Draco Slytherin
```

---

# 10. Creating Patterns with Loops

Loops can generate visual patterns.

### Example

```python
for i in range(3):
    print("#")
```

Output:

```
#
#
#
```

---

### Square Pattern

```python
for i in range(3):
    print("###")
```

Output:

```
###
###
###
```

---

### Nested Loops

Nested loops are loops inside other loops.

Example:

```python
for i in range(3):
    for j in range(3):
        print("#", end="")
    print()
```

Output:

```
###
###
###
```

---

# 11. Using Loops in Functions

Loops can be placed inside functions.

Example:

```python
def main():
    meow(3)

def meow(n):
    for i in range(n):
        print("meow")

main()
```

Output:

```
meow
meow
meow
```

---

# 12. Best Practices with Loops

Good programming practices when using loops:

- Avoid infinite loops unless intentional.
- Use `for` loops when the number of iterations is known.
- Use `while` loops when repetition depends on a condition.
- Keep loop logic simple and readable.

---

# Key Concepts Learned in Week 2

By the end of Week 2 you should understand:

- How to use `while` loops
- How to use `for` loops
- How to use `range()`
- How to iterate through lists
- How to iterate through dictionaries
- How to control loops using `break` and `continue`
- How to create patterns with nested loops

These concepts are fundamental for writing efficient programs and solving algorithmic problems in Python.