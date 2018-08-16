from sentai import units
from sentai.vectors.Vector3 import *


class DynamicBody:
    """ General dynamic body."""
    def __init__(self, position: Vector3, velocity: Vector3, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def momentum(self):
        return self.velocity * self.mass

    def print(self):
        self.position.print()
        self.velocity.print()
        print("Mass:", self.mass)


class BarnesHutBody(DynamicBody):
    """ Body with an associated Cell attribute"""
    def __init__(self, position, velocity, mass):
        DynamicBody.__init__(self, position, velocity, mass)
        self.cell = None

    def assign_cell(self, cell):
        self.cell = cell

    def get_cell(self):
        return self.cell


class CollidingBody(DynamicBody):
    """
    Dynamic body with collision support.
    Assumes a spherical shape for analysis. (Can and should be overridden)
    """
    def __init__(self, position, velocity, mass, radius):
        DynamicBody.__init__(self, position, velocity, mass)
        self.radius = radius
        self.volume = self.get_volume()

    def is_colliding_with(self, other):
        if dist(self.position, other.position) < self.radius:
            return True
        else:
            return False

    def get_volume(self):
        return (4 / 3) * units.pi * (self.radius ** 3)


def process_collision(cb1: CollidingBody, cb2: CollidingBody):
    new_pos = centre_of_mass([cb1, cb2])
    new_mass = cb1.mass + cb2.mass
    new_velocity = (cb1.velocity * cb1.mass + cb2.velocity * cb2.mass) / new_mass
    new_radius = radius_from_volume(cb1.volume + cb2.volume)

    return CollidingBody(new_pos, new_velocity, new_mass, new_radius)


def centre_of_mass(bodies):
    total_mass = 0
    x_tot, y_tot, z_tot = 0, 0, 0
    for body in bodies:
        x_tot += body.position.x * body.mass
        y_tot += body.position.y * body.mass
        z_tot += body.position.z * body.mass
        total_mass += body.mass

    return Vector3(x_tot, y_tot, z_tot) / total_mass


def radius_from_volume(volume):
    return ((3 * volume) / (4 * units.pi)) ** (1 / 3)
