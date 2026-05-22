from collections import Counter
import heapq
# Function definition of topKFrequent
def topKFrequent(nums, k):
    # Count the frequency of each element
    freq = Counter(nums)
    
    # Use a min-heap to keep track of the top k frequent elements
    heap = []
    for num, count in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, num))
        elif count > heap[0][0]:
            heapq.heapreplace(heap, (count, num))
    
    # Extract the elements from the heap
    result = [num for count, num in heap]
    return result

# Driver code
nums = [1, 1, 1, 2, 2, 3]
k = 2           
result = topKFrequent(nums, k)
print("Top k frequent elements:", result)