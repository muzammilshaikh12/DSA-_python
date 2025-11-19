# This function performs selection sort on a list of numbers.
def selection_sort(nums):
    
    # Loop through each index as the starting point of the unsorted part
    for i in range(len(nums)):
        min_index = i  # Assume the current index holds the minimum value
        
        # Find the index of the smallest element in the remaining unsorted portion
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j  # Update min_index when a smaller element is found
        
        # Swap the found minimum element with the element at index i
        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    
    # Return the sorted list
    return nums

# Test the function
print(selection_sort([5, 4, 3, 2, 1]))
print(selection_sort([3, 4, 5, 1, 2]))
