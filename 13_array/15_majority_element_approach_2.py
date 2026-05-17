# Approach 2: Boyer-Moore Majority Vote Algorithm
# Function definition
def find_candidate(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

# Function to check if the candidate is the majority element
def is_majority(nums, candidate):
    cnt = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == candidate:
            cnt += 1
    if cnt > n // 2:
        return 1
    else:
        return 0

# Function defination of printmajorityelement
def print_majority_element(nums):
    candidate = find_candidate(nums)
    if is_majority(nums, candidate):
        print("The majority element is:", candidate)
    else:
        print("No majority element")

# Driver code
nums = [2, 2, 1, 1, 1, 2, 2]
print_majority_element(nums)        