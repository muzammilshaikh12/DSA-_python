from math import sqrt  # Import sqrt to calculate the square root of a number

def print_factors(num):
    factors = []  # List to store all factors of the given number
    
    # Loop from 1 to the square root of the number (inclusive)
    # Because factors repeat after sqrt(num)
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:  # If 'i' divides 'num' evenly, it is a factor
            factors.append(i)  # Add the smaller factor
            
            # Check to avoid adding the same factor twice (for perfect squares)
            if i != (int(num / i)):
                factors.append(int(num // i))  # Add the corresponding larger factor
    
    # Sort the list before returning so factors appear in ascending order
    return sorted(factors)

# Example call: prints all factors of 36
print(print_factors(36))
