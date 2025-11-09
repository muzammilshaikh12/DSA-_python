def palindrome_check(num):
    n = num  # Store the original number to compare later
    reversed_num = 0  # Initialize variable to store the reversed number
    
    # Reverse the digits of the number
    while n > 0:
        digit = n % 10              # Extract the last digit
        reversed_num = reversed_num * 10 + digit  # Append it to reversed_num
        n = n // 10                 # Remove the last digit from n
    
    # Compare the original number and the reversed number
    return num == reversed_num

# Example call — check if 12321 is a palindrome
print(palindrome_check(12321))  # Output: True
