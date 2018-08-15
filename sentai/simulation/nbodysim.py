import numpy as np
from sentai.vectors.Vector3 import *
from sentai.dynamics import DynamicBody, forces

"""
Class containing n-body simulation methods
"""


def celestial_body_sim(bodies, time_step, sim_time):
    """
    Iterates over all bodies, processes their acceleration and adjusts positions over a given timestep. Runs until time
    reaches the simulation time. Returns a list containings lists of position Vector3 objects for each body.
    :param body_list: The list of bodies the simulator will iterate over.
    :param time_step: The amount of time between successive computations.
    :param sim_time: The total amount of simulation time.
    :return: Returns a list of position lists.
    """
    body_list = np.copy(bodies)

    time = 0
    positions = []
    for x in range(0, len(body_list)):
        positions.append([])

    while time < sim_time:
        accelerations = []

        for x in range(0, len(body_list)):
            body_list[x].position = body_list[x].position + (body_list[x].velocity * 0.5 * time_step)
            accelerations.append(forces.calc_net_grav_acceleration(body_list, x))

        for x in range(0, len(body_list)):
            v_new = body_list[x].velocity + accelerations[x]
            r_final = body_list[x].position + (v_new * 0.5 * time_step)
            body_list[x].position = r_final
            body_list[x].velocity = v_new
            positions[x].append(r_final)

        time += time_step
    # print(len(positions), len(positions[0]))

    return positions


def basic_iterator(bodies, time_step, sim_time):
    positions = []
    for x in range(0, len(bodies)):
        positions.append([])

    time = 0
    while time < sim_time:
        accelerations = []
        for x in range(0, len(bodies)):
            accelerations.append(forces.calc_net_grav_acceleration(bodies, x))
        for x in range(0, len(bodies)):
            bodies[x].position += bodies[x].velocity * time_step
            bodies[x].velocity += accelerations[x] * time_step
            positions[x].append(bodies[x].position)

        time += time_step

    return positions
