def extract_digits(num):
    # Loop continues until the number becomes 0
    while num > 0:
        print(num % 10)  # Extract and print the last digit
        num = num // 10  # Remove the last digit by integer division

# Example call — prints each digit of 1234 in reverse order
print(extract_digits(1234))
