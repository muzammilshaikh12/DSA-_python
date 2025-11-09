# This function counts how many times each element from list n appears in list m and prints the frequency.
def checkFreq(m, n):
    my_dict = {}  # Create an empty dictionary to store frequencies of elements from list m
    
    # Count frequency of each element in list m
    for i in m:
        # If element i exists in dictionary, increment its count
        # Otherwise, start with 0 and add 1
        my_dict[i] = (my_dict.get(i) or 0) + 1
    
    # Loop through list n and print frequency of each element based on stored result
    for j in n:
        # If j exists in dictionary, print its frequency
        # If not found, print 0
        print(j, my_dict.get(j) or 0)

# Example usage
checkFreq([1,2,2,3,4,5,1,1,2,1,2,3,4,4,4,3,3], [1,2,3,4,5])
