import math
from utils.stringops import trim_string


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

    def as_unit(self):
        return self / self.mag

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

    def print(self):
        print("Vector2 Object: x:", trim_string(self.x, 5), "y:", trim_string(self.y, 5))


def dot_product(a, b):
    return (a.x * b.x) + (a.y + b.y)


def dist(a, b):
    return Vector2(b.x - a.x, b.y - a.y).mag

