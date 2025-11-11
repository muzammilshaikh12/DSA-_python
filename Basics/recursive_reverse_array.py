# This function reverses part of an array recursively between left and right indices.
def recursive_reverse_array(arr, left, right):
    # Stop when left index crosses or equals right index (reversal complete)
    if left >= right:
        return arr

    # Swap elements at left and right positions
    arr[left], arr[right] = arr[right], arr[left]

    # Move pointers towards middle and continue recursion
    return recursive_reverse_array(arr, left + 1, right - 1)


# Testing
print(recursive_reverse_array([1,2,3,4,5,6,7], 0, 6))  # Full reverse
print(recursive_reverse_array([1,2,3,4,5,6,7], 1, 5))  # Reverse portion
print(recursive_reverse_array([1,2,3,4,5,6,7], 2, 4))  # Reverse portion
print(recursive_reverse_array([1,2,3,4,5,6,7], 3, 3))  # No change (single element)
