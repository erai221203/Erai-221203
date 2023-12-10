import math

# Get all the attributes of the math module
math_attributes = dir(math)

# Filter out non-functions and print the names of the remaining functions
math_functions = [name for name in math_attributes if callable(getattr(math, name))]
print(math_functions)
