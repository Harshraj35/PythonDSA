# Suppose having an array = [20, -30, 10, 5, 7, 0, 29, inf, inf, inf, ..................]
# n - elements are present in the array and the rest of the elements are inf (infinity)

# Function definition
def first_infinite_element(arr):
    low = 0
    high = 0
    n = len(arr)
    # Find the range for binary search by repeated doubling
    while low <= high:
        mid = (low + high) // 2
        if mid >= n or arr[mid] == float('inf'):
            high = mid - 1
            return mid
        else:
            low = mid + 1
    return -1  # Return -1 if no infinite element is found


# Driver code
arr = [20, -30, 10, 5, 7, 0, 29] + [float('inf')] * 1000  # Example array with inf elements
result = first_infinite_element(arr) 
print("The index of the first infinite element is:", result)