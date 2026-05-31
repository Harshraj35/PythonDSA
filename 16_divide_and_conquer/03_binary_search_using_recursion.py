# Using recursion 
# Implementation of binary search
# Time complexity: O(log n)
# Function definition
def binary_search(arr, i, j, x):
    while i <= j:
        mid = i + (j - i) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore the left half
        elif arr[mid] < x:
            # Recursion :-> calling the same function again
            # With different set of parameters
            return binary_search(arr, mid + 1, j, x)
        # If x is smaller, ignore the right half
        else:
            return binary_search(arr, i, mid - 1, x)
        
        # Search element is not present in the array
    return -1


# Driver code
# Sorted array
arr = [2, 5, 10, 14, 18, 22, 27, 35, 40, 59]
x= 40
j = len(arr) - 1
i = 0
# Function calling
result = binary_search(arr, i, j, x)
print("Element is present at index:", result) 