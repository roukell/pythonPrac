"""
shape module. Contains classes Shape, Square, and Circle
"""


# Classes are defined by using the 'class' keyword
class Shape:
    """Shape class: has method move"""

    # __init__ is the instance initializer method (class constructor)
    # variable x and y are created and initialized here
    # methods, like functions, are defined by using the 'def' keyword
    # 'self' is the first argument of any method.
    # When the method is invoked, 'self' is set to the instance that invoked the method.
    # by using 'self' we can access the attributes and methods of the class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY


class Square(Shape):
    """Square class: inherits from Shape"""

    def __init__(self, side=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.side = side

    def area(self):
        """Square area method: returns the area of the circle"""
        return self.side * self.side

    def __str__(self):
        return f"Square has area of {self.side * self.side} at coordinates ({self.x}, {self.y})"


class Circle(Shape):
    """Circle class: inherits from Shape and has method area"""
    pi = 3.14159

    def __init__(self, r=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.radius = r

    def area(self):
        """Circle area method: returns the area of the circle"""
        return self.radius * self.radius * self.pi

    # __str__ method returns a string version of the class and is used by the print function
    def __str__(self):
        return f"Circle of radius {self.radius} at coordinates ({self.x}, {self.y})"
