# Function defination
# Time complexity: O(n^2)
def insertionSort(arr):
    n = len(arr)
    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Driver code
arr = [12, 11, 13, 5, 6]        
sorted_arr = insertionSort(arr)
print("Sorted array:", sorted_arr)