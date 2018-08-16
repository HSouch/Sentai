import numpy as np
from sentai.vectors.Vector3 import *
from sentai.dynamics import forces
from sentai.dynamics.DynamicBody import *
from sentai.simulation.Cell import *

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


def advanced_celestial_body_sim(bodies, time_step, sim_time, max_internal_bodies=5):
    """
    Advanced n-body simulator using Barnes-Hut simulation techniques. Should only be used for simulations with large
    numbers of bodies (1000 plus). Otherwise it is better to use celestial_body_sim().
    :param bodies: List of DynamicBodies to run simulation on
    :param time_step: Amount of time between computations.
    :param sim_time: Duration of simulation.
    :param max_internal_bodies: Number of bodies allowed in each cell. Set to 5 by default. The lower the number the
            more accurate the simulation.
    :return:
    """

    for x in range(0, len(bodies)):
        bodies[x] = BarnesHutBody(bodies[x].position, bodies[x].velocity, bodies[x].mass)

    positions = []
    for x in range(0, len(bodies)):
        positions.append([])
    # Root cell generation.

    root_cell = generate_root_cell(bodies)

    # Create full tree using recursive checks; generate cell list until no cells contain n_bodies > max_internal_bodies
    # Make list of bodies and their associated cells. (Somehow)
    # For each object, get its cell and directly check forces for every object within that cell
    # Calculate forces with dynamic body created at the COM of each subsequent cell (with total mass of cell)
    # Adjust as normal. Update position list.

    return positions
