

class Point2D:
    # Class of two dimensional points 
    def __init__(self, xx, yy): # Constructor 
        self.x = xx
        self.y = yy
    
    def __str__(self): # String method
        return f"(x:{self.x},y:{self.y})"
    
    def __repr__(self): # String representation for other classes
        # usually you want this
        # Classname(attributes)
        return f"Point2D({self.x},{self.y})"


    def __add__(self, other): # + 
        return Point2D(self.x + other.x, self.y + other.y)
    
    def shift_x(self, dx): # move point alongside the x-axis 
        self.x += dx 
    
    def shift_y(self, dy):
        self.y += dy
    
    def shift(self, dx, dy):
        self.shift_x(dx) 
        self.shift_y(dy) 
    
p1 = Point2D(3,5) 
p2 = Point2D(4,5)
p1.shift_x(-1)
p1.shift(2,1)
print(p1)
print([p1, p2+p1, p2+p2])

for i in range(100):
    p = Point2D(i,i+1)
    print(p)
