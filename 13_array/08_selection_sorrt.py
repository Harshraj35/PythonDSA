# Function defination
# Time complexity: O(n^2)
def selectionSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Driver code
arr = [64, 25, 12, 22, 11]  
sorted_arr = selectionSort(arr)
print("Sorted array:", sorted_arr)