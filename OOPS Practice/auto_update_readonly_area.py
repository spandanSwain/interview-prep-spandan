import math
# make the area readonly, and make sure that each time radius is changed area changes dynamically
class Circle:
    def __init__(self, r: int | float):
        self._radius = max(0, r)
    
    # set radius
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value: int | float):
        # self._radius = 0 if value<0 else value
        self._radius = max(0, value)
        
    # set readonly area
    @property
    def area(self):
        # usually _radius is used as it doesn't go through any getter method, but radius goes through a getter method
        return math.pi * self._radius ** 2

c = Circle(1)
print(c.area)
c1 = Circle(2)
print(c1.area)