def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(6)
print(f"The factorial of 5 is: {result}")
