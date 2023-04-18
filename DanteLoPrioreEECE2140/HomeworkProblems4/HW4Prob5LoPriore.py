import numpy as np 
import matplotlib.pyplot as plt

# Dante LoPriore
# March 28, 2023
# PS4: Problem 5

# Purpose: to produce a class Circle, that creates an object 
# with two data attributes center and radius, and a method draw

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


# to represent the circle class   
class Circle():

    # constructor
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    @property # getter method
    def center(self):
        return self._center #protected instance attribute
    
    @center.setter #setter method
    def center(self, inCenter):
        if isinstance(inCenter, Point):
            self._center = inCenter
        else:
            raise ValueError("Given input for the center must be a type center")
    
    @property # becomes property of your class
    def radius(self): #getter method
        return self._radius #returns protected attribute

    @radius.setter #setter method
    def radius(self, rad): # checks whether the radius is positive 
        if(rad >= 0): 
            self._radius = rad
        else: 
            raise ValueError("Radius Should be Positive")
    
    def __str__(self):
        return f'The Circle has a the coordinates of ({self.center.x}, {self.center.y}, {self.center.z}) with a radius of {self.radius}'
    
    # creates a circle on the plot 
    def draw(self):

        plt.figure()
        plt.grid()
        # creates the x limits based on the given radius
        min_center_x_radius = self.center.x - self.radius
        max_center_x_radius = self.center.x + self.radius

        # set the x and y axis for the project circle on the plot 
        x_axis = np.linspace(min_center_x_radius, max_center_x_radius, 100000)
        y_axis = self.center.y + np.sqrt(((self.radius)**2) - ((x_axis - self.center.x)**2)) 

        # plots the first half or top part of the circle
        plt.plot(x_axis, y_axis, "r-")

        # plots the second half or bottom part of the circle 
        # this function will connected the bottom and the top of the circle
        plt.plot(x_axis, -(y_axis) + 2*self.center.y, "r-")

        # labeling the circle being ploted 
        plt.ylabel('Y')
        plt.xlabel('X')
        plt.title("Drawing a Circle Graph for (x-xc)^2 + (y-yc)^2 = r^2", loc='center')
        plt.show()

point1 = Point(1, 1)
point2 = Point(20, -10)
point3 = Point(-10, 10)
cir1 = Circle(point1, 1)
cir2 = Circle(point1, 20)
cir3 = Circle(point3, 1)
#cir1 = Circle(p3, -10) won't work
print(cir1.draw())
print(cir1)

