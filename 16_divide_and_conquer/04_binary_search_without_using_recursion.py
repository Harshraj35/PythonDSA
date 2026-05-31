# Without using recursion
# Function defination
# Time complexity: O(log n)
def binary_search(arr, i, j, x):
    while i <= j:
        mid = i + (j - i) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore the left half
        elif arr[mid] < x:
            i = mid + 1
        # If x is smaller, ignore the right half
        else:
            j = mid - 1
        
    # Search element is not present in the array
    return -1

# Driver code
# Sorted array
arr = [2, 5, 10, 14, 18, 22, 27, 35, 40, 59]
x= 22
j = len(arr) - 1
i = 0
# Function calling
result = binary_search(arr, i, j, x)
print("Element is present at index:", result)