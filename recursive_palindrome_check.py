# This function checks whether a string is a palindrome using recursion
def recursive_palindrome_check(string, left=0, right=None):
    # Initialize right index during first call
    if right is None:
        right = len(string) - 1

    # Stop condition: pointers crossed means it's a palindrome
    if left >= right:
        return True

    # If characters don't match, it's not a palindrome
    if string[left] != string[right]:
        return False

    # Recur by shrinking the window
    return recursive_palindrome_check(string, left + 1, right - 1)


# Testing
print(recursive_palindrome_check("madam"))     # True
print(recursive_palindrome_check("racecar"))   # True
print(recursive_palindrome_check("hello"))     # False
