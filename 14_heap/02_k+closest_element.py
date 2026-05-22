from heapq import heappush, heappop
from multiprocessing import heap
# Function definition of kClosest
# get_distance calculates the distance of a point from the origin
def get_distance(point):
    x, y = point
    return x**2 + y**2

def kClosest(points, k):
    # Create a max-heap to keep track of the k closest points
    min_heap = []
    for point in points:
        distance = get_distance(point)
        if len(min_heap) < k:
            heappush(min_heap, (-distance, point))
        elif distance < -min_heap[0][0]:
            heappop(min_heap)
            heappush(min_heap, (-distance, point))
    
    # Extract the points from the heap
    result = [point for distance, point in min_heap]
    return result

# Driver code
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2   
result = kClosest(points, k)
print("K closest points to the origin:", result)