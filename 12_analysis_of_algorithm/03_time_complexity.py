def main(n):
    # O(n^2) - Quadratic Time Complexity
    y = 7
    z = 3
    x = y + z
    
    for i in range(0, n):
        for j in range(0, n):
            x = y + z
    print("Result:", x)