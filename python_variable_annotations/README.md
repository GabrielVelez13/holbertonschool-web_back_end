# Learning Static Typing in Python

Welcome to the educational repository for learning static typing in Python! In this repository, you will find step-by-step instructions, examples, and fun facts about static typing in Python.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Basic Syntax](#basic-syntax)
- [Type Hints](#type-hints)
- [Type Checking](#type-checking)
- [Advanced Topics](#advanced-topics)
- [Fun Facts](#fun-facts)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Static typing is a feature in Python that allows you to specify the type of a variable, function argument, or return value. By explicitly declaring types, you can catch type-related errors early and improve code readability. This section provides a brief introduction to static typing in Python and explains its benefits.

## Getting Started

To get started with static typing in Python, follow these steps:

1. Install Python 3.6 or later, if you haven't already.
2. Set up a virtual environment for your project.
3. Install the `mypy` type checker using pip: `pip install mypy`.
4. Create a new Python file and import the necessary modules.

# Basic Syntax
Static typing in Python involves annotating variables, function arguments, and return types with type hints. Here's an example of basic syntax:

# Annotating variables
```py
name: str = "John"

age: int = 25

is_student: bool = True
```
# Annotating function arguments and return types
```py
def greet(name: str) -> str:
    return f"Hello, {name}!"
```
# Type hints can also be used with collections
```py
from typing import List, Tuple

numbers: List[int] = [1, 2, 3, 4, 5]

coordinates: Tuple[float, float] = (10.0, 20.0)
```
# Type hints can be used with classes and class attributes
```py
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I'm {self.age} years old."
```
# Type hints can be used with optional values
```py
from typing import Optional

def get_name() -> Optional[str]:
    return "John"
```
# Type hints can be used with generic types
```py
from typing import List, Union

def process_data(data: List[Union[int, str]]) -> None:
    for item in data:
        if isinstance(item, int):
            print(f"Processing integer: {item}")
        elif isinstance(item, str):
            print(f"Processing string: {item}")
```