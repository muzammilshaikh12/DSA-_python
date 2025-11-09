from math import *  # Import all math functions (used here for log10)

def armstrong_number(num):
    n = num  # Store original number in 'n' for manipulation
    # Find the number of digits in 'num'
    # Example: if num = 371, length = 3
    length = int(log10(n)) + 1  
    
    check_value = 0  # To accumulate the sum of each digit raised to 'length'
    
    # Extract digits one by one
    while n > 0:
        digit = n % 10  # Get the last digit
        check_value += digit ** length  # Add (digit^length) to check_value
        n = n // 10  # Remove the last digit
    
    # Return True if the sum equals the original number
    return check_value == num

# Example usage — check if 371 is an Armstrong number
print(armstrong_number(371))  # Output: True
