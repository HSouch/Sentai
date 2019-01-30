import random
# from sentai.vectors.Vector3 import *
from sentai.dynamics.DynamicBody import *

"""
Random Generation Methods for N-Body simulation.
"""


def generate_random_bodies(num_bodies: int, max_dist: float, max_velocity: float, min_mass: float, max_mass: float):
    """
    Create a list of bodies with specified locations, velocities, and masses.
    :param num_bodies:
    :param max_dist:
    :param max_velocity:
    :param min_mass:
    :param max_mass:
    :return:
    """
    bodies = []

    for n in range(0, num_bodies):
        pos = Vector3(random.uniform(-max_dist, max_dist), random.uniform(-max_dist, max_dist),
                      random.uniform(-max_dist, max_dist))
        vel = Vector3(random.uniform(-max_velocity, max_velocity), random.uniform(-max_velocity, max_velocity),
                      random.uniform(-max_velocity, max_velocity))
        mass = random.uniform(min_mass, max_mass)
        bodies.append(DynamicBody(pos, vel, mass))

    return bodies
