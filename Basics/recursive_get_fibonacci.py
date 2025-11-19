# This function returns the nth Fibonacci number using recursion and accumulator variables.
def recursive_get_fibonacci(num, count=1, current=1, previous=0):

    # When count reaches the required position, return the current Fibonacci value
    if count == num:
        return current

    # Update Fibonacci numbers: next = current + previous
    current, previous = current + previous, current

    # Move to the next index
    count += 1

    # Recursive call with updated values
    return recursive_get_fibonacci(num, count, current, previous)


# Testing
print(recursive_get_fibonacci(5))
print(recursive_get_fibonacci(6))
print(recursive_get_fibonacci(7))
print(recursive_get_fibonacci(8))
