# Function definition
def find_max_and_min(arr, i, j):
    # Small problem
    # Single element present in an array
    if i == j:
        max_val = arr[i]
        min_val = arr[i]
    # Two elements present in an array
    elif j == i + 1:
        if arr[i] < arr[j]:
            max_val = arr[j]
            min_val = arr[i]
        else:
            max_val = arr[i]
            min_val = arr[j]        
    # Big problem
    else:
        mid = (i + j) // 2
        # Recursive calls to find the maximum and minimum in the left and right halves of the array using divide and conquer approach
        max_l, min_l = find_max_and_min(arr, i, mid)
        max_r, min_r = find_max_and_min(arr, mid + 1, j)
        # Compare the maximum values obtained from the left and right halves to find the overall maximum and minimum values in the array
        if max_l < max_r:
            max_val = max_r
        else:
            max_val = max_l  
        # Compare the minimum values obtained from the left and right halves to find the overall minimum value in the array
        if min_l < min_r:
            min_val = min_l
        else:
            min_val = min_r
    return max_val, min_val        



# Driver code
arr = [70, 10, 45, 16, 29, 30, 35, 20]
i = 0
j = len(arr) - 1
# Function calling
max_val, min_val = find_max_and_min(arr, i, j)
print("Maximum and minimum elements in an array is:", max_val, min_val)