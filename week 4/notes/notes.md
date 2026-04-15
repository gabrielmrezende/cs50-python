# CS50P — Week 4: Libraries

## Overview

Week 4 introduces **libraries**, which are collections of prewritten code that programmers can reuse instead of writing everything from scratch.

Python has many **built-in libraries**, and developers can also install **third-party libraries** created by others.

This week teaches how to:

- Import modules
- Use built-in Python libraries
- Install external packages
- Work with APIs
- Read command-line arguments

---

# 1. What is a Library?

A **library** is a file or collection of files containing functions and code that can be reused.

Example:

Instead of writing your own random number generator, you can use Python’s built-in library.

```python
import random

number = random.randint(1, 10)
print(number)
```

The `random` module provides tools for generating random values.

---

# 2. Importing Modules

Python uses the keyword `import` to load a library.

Basic syntax:

```python
import module_name
```

Example:

```python
import random

print(random.randint(1, 10))
```

Here Python loads the `random` module and allows access to its functions.

---

# 3. Importing Specific Functions

Instead of importing an entire module, you can import a specific function.

Example:

```python
from random import randint

print(randint(1, 10))
```

Now you can use `randint()` directly.

---

# 4. Importing with Aliases

Sometimes modules have long names. Python allows creating **aliases**.

Example:

```python
import random as r

print(r.randint(1, 10))
```

This is helpful for large libraries.

---

# 5. Built-in Python Libraries

Python includes many built-in modules.

Examples:

| Module | Purpose |
|------|------|
| `random` | Generate random numbers |
| `statistics` | Perform statistical calculations |
| `sys` | Access system and command-line features |
| `datetime` | Work with dates and time |

---

# 6. The `random` Module

The `random` module allows generating random values.

### Random Integer

```python
import random

number = random.randint(1, 10)
print(number)
```

Generates a random integer between 1 and 10.

### Random Choice

```python
import random

coin = random.choice(["heads", "tails"])
print(coin)
```

Selects a random element from a list.

### Shuffle a List

```python
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards)
```

Randomly rearranges the list.

---

# 7. The `statistics` Module

The `statistics` module allows performing mathematical analysis.

Example:

```python
import statistics

numbers = [100, 90, 80, 70]
average = statistics.mean(numbers)

print(average)
```

Common functions:

| Function | Description |
|------|------|
| `mean()` | Average |
| `median()` | Middle value |
| `mode()` | Most frequent value |

---

# 8. Command-Line Arguments (`sys.argv`)

Programs can receive input from the **command line**.

Example:

```python
import sys

print(sys.argv)
```

If the program is run as:

```
python script.py David
```

Output:

```
['script.py', 'David']
```

`sys.argv` is a **list containing command-line arguments**.

---

# 9. Checking Command-Line Arguments

Example:

```python
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello,", sys.argv[1])
```

This program expects exactly **one argument**.

---

# 10. Looping Through Arguments

You can iterate through command-line arguments.

Example:

```python
import sys

for arg in sys.argv:
    print(arg)
```

---

# 11. Installing External Libraries (pip)

Python allows installing libraries from the internet using **pip**.

Example:

```
pip install requests
```

This installs the **:contentReference[oaicite:1]{index=1}** library.

---

# 12. Using External Libraries

Example with the **:contentReference[oaicite:2]{index=2}** library:

```python
import requests

response = requests.get("https://api.github.com")
print(response.json())
```

This sends an **HTTP request** to an API and prints the returned data.

---

# 13. Working with APIs

An **API (Application Programming Interface)** allows programs to communicate with external services.

Example:

Getting the price of Bitcoin from an API.

```python
import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()

price = data["bpi"]["USD"]["rate"]
print(price)
```

Steps:

1. Send request
2. Receive response
3. Convert JSON data
4. Extract needed information

---

# 14. JSON Data

Many APIs return data in **JSON format**.

Example JSON:

```json
{
    "name": "Bitcoin",
    "price": 65000
}
```

In Python:

```python
data = response.json()
print(data["price"])
```

JSON objects behave like **Python dictionaries**.

---

# 15. Handling Request Errors

Network requests can fail, so they should be wrapped in exception handling.

Example:

```python
import requests

try:
    response = requests.get("https://api.example.com")
    data = response.json()
except requests.RequestException:
    print("Request failed")
```

This prevents the program from crashing if the network fails.

---

# 16. Example: Bitcoin Price Calculator

Example program using an API and command-line arguments.

```python
import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
data = response.json()

price = float(data["data"]["priceUsd"])
total = bitcoins * price

print(f"${total:,.4f}")
```

This program:

1. Reads the number of bitcoins from the command line
2. Gets the current Bitcoin price from an API
3. Calculates the total value

---

# Key Concepts Learned in Week 4

By the end of Week 4 you should understand:

- What libraries are
- How to import modules
- How to import specific functions
- How to create aliases
- How to use built-in libraries
- How to install external libraries with `pip`
- How to work with APIs
- How to parse JSON data
- How to use command-line arguments (`sys.argv`)
- How to handle network request errors

Libraries allow programmers to **reuse powerful tools**, making programs much faster to build and more capable.