import random
from sentai.vectors.Vector3 import *
from sentai.dynamics.DynamicBody import *

"""
Random Generation Methods for N-Body simulation.
"""


def generate_random_bodies(num_bodies, max_dist, max_velocity, min_mass, max_mass):
    bodies = []

    for n in range(0, num_bodies):
        dist = Vector3(random.uniform(-max_dist, max_dist), random.uniform(-max_dist, max_dist),
                       random.uniform(-max_dist, max_dist))
        vel = Vector3(random.uniform(-max_velocity, max_velocity), random.uniform(-max_velocity, max_velocity),
                      random.uniform(-max_velocity, max_velocity))
        mass = random.uniform(min_mass, max_mass)
        bodies.append(DynamicBody(dist, vel, mass))

    return bodies
