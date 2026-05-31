# Find the power of an element using divide and conquer when n >= 1
# Function definition
# Time complexity: O(log n)
def find_power_of_element(a, n):
    # Small problem
    if n == 1:
        return a
    else:
        # Big problem
        mid = n // 2
        # Recursive call
        b = find_power_of_element(a, mid)
        result = b * b
        # Even power
        if n % 2 == 0:
            return result
        else:
            return result * a
        
# Driver code
a = 2
n = 10
# Function calling
result = find_power_of_element(a, n)
print("The power of an element is:", result)