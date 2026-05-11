arr = [2, 1, 8, 9, 12, 15, 11, 19]
# Random access
print(arr[4]) # Output: 12

# search for an element "15" and if it's present in an array, return the index of that element
# suppose the searching element is not present in an array, then return -1
# function definition
def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Driver code
x = 15
result = linearsearch(arr, x)
if result != -1:
    print("Element is present at index", result)

# Insert an element "5" at index 2
# List.insert() method is used to insert an element at a specific index in a list. It takes two arguments: the index where the element should be inserted and the element itself.
# Time complexity: O(n) because in the worst case, we may need to shift all the elements to the right to make space for the new element.
arr.insert(2, 5)
print(arr) # Output: [2, 1, 5, 8, 9, 12, 15, 11, 19]

# Remove an element "8" from the array
# Time complexity: O(n) because in the worst case, we may need to search through the entire list to find the element to remove.
# List.remove() method is used to remove the first occurrence of a specified value from a list. It takes one argument: the value to be removed. If the value is not found in the list, it raises a ValueError.
arr.remove(8)
print(arr) # Output: [2, 1, 5, 9, 12, 15, 11, 19]

# Count the frequency of an element present inside the array
arr.count(2) # Output: 1
print(arr) # Output: [2, 1, 5, 9, 12, 15, 11, 19]

# Delete an element providing the index
arr.pop(4) # Output: 12
print(arr) # Output: [2, 1, 5, 9, 15, 11, 19]

# Sort the array in ascending order
arr.sort()
print(arr) # Output: [1, 2, 5, 9, 11, 15, 19]

# To extract the index of any given element in an array
arr.index(11) # Output: 4
print(arr) # Output: [1, 2, 5, 9, 11, 15, 19]

# To extent the original array
arr.extend([2, 5, 7, 10])
print(arr) # Output: [1, 2, 5, 9, 11, 15, 19, 2, 5, 7, 10]

# To reverse the entire list
arr.reverse()
print(arr) # Output: [10, 7, 5, 2, 19, 15, 11, 9, 5, 2, 1]