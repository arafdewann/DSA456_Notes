# Python Basics

## Introduction
Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

## Setting Up Python
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Install Python and verify using:
   ```sh
   python --version
   ```

## Basic Syntax
### Hello World
```python
print("Hello, World!")
```

### Variables and Data Types
```python
x = 10         # Integer
y = 3.14       # Float
name = "Arafat"  # String
is_valid = True # Boolean
```

### Type Checking
```python
print(type(x))  # Output: <class 'int'>
```

## Operators
### Arithmetic Operators
```python
x = 10
y = 3
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x // y) # Floor Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation
```

### Comparison Operators
```python
print(x > y)  # Greater than
print(x < y)  # Less than
print(x == y) # Equal to
print(x != y) # Not equal to
```

### Logical Operators
```python
print(x > 5 and y < 5)  # AND
print(x > 5 or y > 5)   # OR
print(not(x > 5))       # NOT
```

## Control Flow
### If-Else Statements
```python
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```

### Loops
#### For Loop
```python
for i in range(5):
    print(i)
```
#### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Arafat"))
```

## Data Structures
### Lists
```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Add element
print(numbers)
```

### Tuples
```python
tuple_data = (1, 2, 3)
print(tuple_data[0])
```

### Dictionaries
```python
student = {"name": "Arafat", "age": 25}
print(student["name"])
```

### Sets
```python
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)
```

## File Handling
```python
with open("test.txt", "w") as file:
    file.write("Hello, World!")
```

## Exception Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Modules and Libraries
```python
import math
print(math.sqrt(25))
```

## Conclusion
This is a basic introduction to Python covering fundamental concepts. Continue exploring advanced topics like OOP, decorators, and multithreading!
