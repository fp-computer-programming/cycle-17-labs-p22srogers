# Author: SMR (AMDG) 04/29/22
import math

class Circle:
    """ Circle class represents a circle """
    def __init__(self):
        """ Creates a new circle with radius 3 """
        self.radius = 3
    def area(self):
        """ Calculates the area of circle """
        return self.radius ** 2 * math.pi

my_circle = Circle()

print(my_circle.area())