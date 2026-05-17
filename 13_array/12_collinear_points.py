# Approach 1: Using slope formula
# Function definition   
def is_collinear(x1, x2, x3,y1, y2, y3):
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        print("The points are collinear")
    else:
        print("The points are not collinear")

# Driver code
x1, x2, x3, y1, y2, y3 = 1, 1, 1, 6, 0, 9
is_collinear(x1, x2, x3, y1, y2, y3)     

