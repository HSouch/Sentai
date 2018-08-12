import math


class Vector3:
    """
    Class to represent a 3-Dimensional Vector
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.mag = self.mag()

    def mag(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def as_unit(self):
        return self / self.mag

    def __add__(self, other):
        return Vector3(self.x + other.x,
                       self.y + other.y,
                       self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x,
                       self.y - other.y,
                       self.z - other.z)

    def __mul__(self, const):
        return Vector3(self.x * const,
                       self.y * const,
                       self.z * const)

    def __truediv__(self, const):
        if const != 0:
            return Vector3(self.x / const,
                           self.y / const,
                           self.z / const)
        else:
            print("Error. Attempting to divide by zero.")


def dot_product(a, b):
    return (a.x * b.x) + (a.y + b.y) + (a.z + b.z)


def cross_product(a, b):
    return Vector3((a.y * b.z) - (b.y * a.z),
                   (b.x * a.z) - (b.z * a.x),
                   (b.y * a.x) - (b.x * a.y))


def dist(a, b):
    return Vector3(b.x - a.x, b.y - a.y, b.z - a.z).mag
