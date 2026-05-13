def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Driver code
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 50
result = linearsearch(arr, x)
if result != -1:
    print("Element is present at index", result)