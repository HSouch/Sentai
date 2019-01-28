import numpy as np
from dynamics import forces
from dynamics.DynamicBody import *
from simulation.Cell import *

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


def advanced_celestial_body_sim(init_bodies, time_step, sim_time, max_contained_bodies=5):
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
    bodies = np.copy(init_bodies)

    for x in range(0, len(bodies)):
        bodies[x] = BarnesHutBody(bodies[x].position, bodies[x].velocity, bodies[x].mass)
        bodies[x].id = x

    positions = []
    for x in range(0, len(bodies)):
        positions.append([])

    cells = split_cells(generate_root_cell(bodies), max_contained_bodies=5)
    print("Number of bodies:", len(bodies), " | Final:", len(cells))

    for x in range(0, len(cells)):  # Assign cell id
        cells[x].id = x
        for body in cells[x].bodies:
            body.assign_cell(cells[x])

    for cell in cells:
        cell.centre_of_mass = cell.get_centre_of_mass()
        cell.centre_of_mass.print()


    # for body in bodies:
    #     local_cell = body.cell
    #     print(body.cell)
    #     for near_body in local_cell.bodies:
    #         if body.id != near_body.id:
    #             body.acceleration += forces.grav_acceleration(body, near_body)
    #     for cell in cells:
    #         if cell.id != local_cell.id:
    #             body.acceleration += forces.grav_acceleration(body, DynamicBody(cell.centre_of_mass, Vector3(0, 0, 0),
    #                                                                             cell.total_mass()))

    # Adjust as normal. Update position list.

    return positions
