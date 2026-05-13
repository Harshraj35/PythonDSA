# Implementation of binary search using recursion method
# Function defination
def binarysearch(arr, i, j, x):
    while i <= j:
        mid = i + (j - i) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            # update the i parameter
            i = mid + 1
        else:
            # update the j parameter
            j = mid - 1
    # Searching element is not present in the array    
    return -1

# Driver code
# Sorting array
arr = [2, 5, 10, 14, 18, 22, 27, 35, 40, 59]
x = 14
i = 0
j = len(arr) - 1
# Function call
result = binarysearch(arr, i, j, x)
print("Searching element is present at index", result)