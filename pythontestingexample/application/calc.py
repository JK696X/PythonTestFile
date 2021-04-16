# Use this for testing absolute/relative path
import sys
import os

absFilePath = os.path.abspath(__file__)
print(absFilePath)
fileDir = os.path.dirname(os.path.abspath(__file__))
print(fileDir)
parentDir = os.path.dirname(fileDir)
print(parentDir)
sys.path.append(parentDir)


def add(x, y):
    # Add Function
    return x + y


def subtract(x, y):
    # Subtract Function
    return x - y


def multiply(x, y):
    # Multiply function
    return x * y


def divide(x, y):
    # Divide Function
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
