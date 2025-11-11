# This function calculates factorial of a number using functional recursion.
def recursive_factorial(n):
    # Base condition: when n reaches 1, return 1 and stop recursion
    if n == 1:
        return 1
    
    # Recursive call: multiply n with factorial of (n-1)
    return n * recursive_factorial(n - 1)

# Testing the function
print(recursive_factorial(3))
print(recursive_factorial(4))
print(recursive_factorial(5))
print(recursive_factorial(6))

# This function calculates factorial using parameterized recursion and an accumulator (tail recursion style)
def recursive_factorial(n, fact=1):
    # Base case: when n reaches 1, return the accumulated factorial value
    if n == 1:
        return fact
    
    # Multiply current number with accumulated factorial
    fact = fact * n
    
    # Recursive call with decremented n and updated factorial
    return recursive_factorial(n - 1, fact)

# Testing the function with multiple values
print(recursive_factorial(3))  # Output: 6
print(recursive_factorial(4))  # Output: 24
print(recursive_factorial(5))  # Output: 120
print(recursive_factorial(6))  # Output: 720

