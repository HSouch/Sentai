import numpy as np
from sentai.vectors.Vector3 import *
from sentai.dynamics import DynamicBody, forces

"""
Class containing n-body simulation methods
"""


def celestial_body_sim(bodies, time_step, sim_time):
    active = True
    positions = []
    for x in range(0, len(bodies)):
        positions.append([])

    time = 0
    while time < sim_time:
        accelerations = []
        for x in range(0, len(bodies)):
            accelerations.append(forces.calc_net_grav_acceleration(bodies, x))
        for x in range(0, len(bodies)):
            if active:
                bodies[x].position += bodies[x].velocity * time_step
                bodies[x].velocity += accelerations[x] * time_step
                active = False
            else:
                bodies[x].velocity += accelerations[x] * time_step
                bodies[x].position += bodies[x].velocity * time_step
                active = True
            positions[x].append(bodies[x].position)

        time += time_step

    return positions
