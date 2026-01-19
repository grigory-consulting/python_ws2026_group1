

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

    # TODO 
    # write a function that calculates the distance from the point to origin (zero)
    def distance_0(self):
        return (self.x**2 + self.y**2)**0.5 




p1 = Point2D(3,5) 
p2 = Point2D(4,5)
p1.shift_x(-1)
p1.shift(2,1)
print(p1)
print([p1, p2+p1, p2+p2])
print(p1.distance_0())

#for i in range(100):
#    p = Point2D(i,i+1)
#    print(p)


class Point3D(Point2D): # by inheritance from Point2D.
    # Point2D is superclass (parent), Point3D is subclass (child)
    def __init__(self, xx, yy, zz):
        super().__init__(xx,yy) # Point2D creation 
        self.z = zz
    
    def __str__(self): 
        return f"(x:{self.x},y:{self.y},z:{self.z})"
    
    def __repr__(self): 
        return f"Point3D({self.x},{self.y}, {self.z})"

    def shift_z(self, dz):
        self.z += dz
    
    def shift(self, dx, dy,dz):
        super().shift(dx,dy) # from Point2D
        self.shift_z(dz)     
    
    # TODO 
    # write a function that calculates the distance from the point to origin (zero)
    def distance_0(self):
        #return (self.x**2 + self.y**2 + self.z**2)**0.5 

        val = super().distance_()**2 # self.x**2 + self.y**2
        val += self.z**2
        return val ** 0.5

     
p4 = Point3D(1,2,3)
p4.shift(0.4,2,-3)
print(p4)