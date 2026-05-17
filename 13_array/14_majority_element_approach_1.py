# Approach 1: Dictionary data structure
from collections import Counter as counter
# Function definition
def majority_element(nums):
    counts = counter(nums)
    print(counts)
    return max(counts, key=counts.get)

# Driver code
nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print(result)