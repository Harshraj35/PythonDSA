# Function defination
def searchSortedmatrix(matrix, target):
    # Number of rows
    m = len(matrix)
    if m == 0:
        return False
    # Number of columns
    n = len(matrix[0])
    # Binary search implementation
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        # Convert 1D index to 2D coordinates
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Test cases
matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target1 = 3
print(searchSortedmatrix(matrix1, target1))  # Output: True 
matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target2 = 13    
print(searchSortedmatrix(matrix2, target2))  # Output: False