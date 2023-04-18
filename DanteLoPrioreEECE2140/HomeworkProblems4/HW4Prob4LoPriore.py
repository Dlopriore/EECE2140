import numpy as np 

# Dante LoPriore
# March 28, 2023
# PS4: Problem 4

# Purpose: to produce a class Point with desired methods

# to represent the Point class
class Point():
    
    # constructor
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z 
    
    @property # read only property where getter method but no setter method
    def r(self): # calulates the distance of the Point object from the origin
        return np.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def __str__(self): #prints object
        return f'({self.x}, {self.y}, {self.z})'
    
    def __eq__(self, other): #operator overrides equals 
        # to determine whether the object have the same distance from the orgin as each other
        if isinstance(other, Point): return (self.r == other.r) 

    def __lt__(self, other): #operator override less than based on distance from the orgin
        if isinstance(other, Point): return (self.r < other.r) 
    
    def __le__(self, other):  #operator override greater than or equal to based on distance from the orgin
        return self.r <= other.r
    
    def __ne__(self, other):  #operator override not equal to based on distance from the orgin
        return not self.__eq__(other)
    
    def __gt__(self, other):  #operator override greater than based on distance from the orgin
        return not self.__lt__(other) and self.__ne__(other)
    
    def __ge__(self, other):  #operator override greater than or equal to based on distance from the orgin
        return self.r >= other.r
    
    def __add__(self, other): #operator override built-in addition 
        if isinstance(other, Point):
            new_point = Point(self.x + other.x, self.y + other.y, self.z + other.z)
            return new_point
        else:
            return "The + operator cannot accept the data type of other"
    
    def __iadd__(self, other): #operator override addition assignment
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y 
            self.z += other.z
            return self
        else:
            return "The += operator cannot accept the data type of other"
    
    # output coordinates as a dictionary
    def asdict(self):
        return {'x': self.x, 'y': self.y, 'z': self.z}
    
    

p1 = Point(1, 2, 3)

p2 = Point(2, 4, 6)
print(p2)

p3 = p1 + p2
print(p3)

p1 += p3
print(p1)

print(p1 == p1)
print(p1 == p2)
print(p1 != p2)
print(p1 != p2)
print(p1 > p2)
print(p1 < p2)
print(p1 <= p2)
print(p2 <= p2)
print(p2.r)
#p2.r = 9 would not work 
print(p2.r)
