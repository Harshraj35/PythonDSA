# Implementation of Ternary Search in Python
# Recurrence relation: T(n) = T(n/3) + c
# Function definition
def ternarySearch(arr, left, right, target):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Check if target is present at mid1
        if arr[mid1] == target:
            return mid1
        # Check if target is present at mid2
        if arr[mid2] == target:
            return mid2
        
        # If target is less than mid1, search in the left third
        if target < arr[mid1]:
            return ternarySearch(arr, left, mid1 - 1, target)
        # If target is greater than mid2, search in the right third
        elif target > arr[mid2]:
            return ternarySearch(arr, mid2 + 1, right, target)
        # If target is between mid1 and mid2, search in the middle third
        else:
            return ternarySearch(arr, mid1 + 1, mid2 - 1, target)
    
    # Target was not found in the array
    return -1

# Test cases
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target1 = 5
print(ternarySearch(arr1, 0, len(arr1) - 1, target1))  # Output: 4

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 15
print(ternarySearch(arr2, 0, len(arr2) - 1, target2))  # Output: -1