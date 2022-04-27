# Author: SMR (AMDG) 04/29/22
import math

class Circle:
    """ Circle class represents a circle: """
    def __init__(self):
        """ Creates a new circle with a radius of 3: """
        self.radius = 3
    def get_diameter(self):
        """ Calculates the diameter of circle: """
        return self.radius * 2
    def get_perimeter(self):
        """ Calculates the perimeter of circle: """
        return self.get_diameter() * math.pi

my_circle = Circle()

print(my_circle.radius)
print(my_circle.get_diameter())
print(my_circle.get_perimeter())