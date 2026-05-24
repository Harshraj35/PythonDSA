# Count of number of ways to reach upstairs
# Using fibonacci series
# Function helper definition   
def helper(n):
    if n <= 1:
        return 1
    else:
        return helper(n - 1) + helper(n - 2)

# Function definition
def count_number_of_ways(s):
    return helper(s + 1)

# Driver code
s = 4
result = count_number_of_ways(s)
print("Number of ways to reach upstairs:", result)