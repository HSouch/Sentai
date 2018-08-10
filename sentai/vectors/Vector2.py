import math


class Vector2:
    """
    Class to represent a 2-Dimensional Vector
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mag = self.mag()

    def mag(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __add__(self, other):
        return Vector2(self.x + other.x,
                       self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x,
                       self.y - other.y)

    def __mul__(self, const):
        return Vector2(self.x * const,
                       self.y * const)

    def __truediv__(self, const):
        if const != 0:
            return Vector2(self.x / const,
                           self.y / const)
        else:
            print("Error. Attempting to divide by zero.")


def dot_product(a, b):
    return (a.x * b.x) + (a.y + b.y)


def dist(a, b):
    return Vector2(b.x - a.x, b.y - a.y).mag
