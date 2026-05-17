# Approach 2: Using area of triangle
# Function definition   
def is_collinear(x1, x2, x3,y1, y2, y3):
    area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    if area == 0:
        print("The points are collinear")
    else:
        print("The points are not collinear")

# Driver code
x1, x2, x3, y1, y2, y3 = 1, 1, 1, 6, 0, 9
is_collinear(x1, x2, x3, y1, y2, y3)
        