from sentai.dynamics.DynamicBody import *
from sentai.vectors.Vector3 import Vector3


def grav_force(db1: DynamicBody, db2: DynamicBody):
    """
    Calculates the gravitational force on db1 due to db2
    :param db1: The active dynamic body.
    :param db2: The interacting dynamic body. The force will point in the direction of db2.
    :return:
    """
    distance_vector = db2.position - db1.position
    try:
        force = units.g * db1.mass * db2.mass / (distance_vector.mag ** 2)
    except ZeroDivisionError:
        return Vector3(0, 0, 0)
    return distance_vector.as_unit() * force


def grav_acceleration(db1: DynamicBody, db2: DynamicBody):
    """ Calculates the acceleration of db1 due to the gravitational force of db2. """
    force = grav_force(db1, db2)
    return force / db1.mass


def calc_net_grav_acceleration(bodies, x):
    """
    Calculates the net gravitational acceleration for the xth particle in a list of Dynamic Bodies.
    :param bodies:
    :param x:
    :return:
    """
    net_acceleration = Vector3(0, 0, 0)
    for y in range(0, len(bodies)):
        if y == x:
            continue
        net_acceleration += grav_acceleration(bodies[x], bodies[y])
    return net_acceleration


def coulomb_force(db1: Molecule, db2: Molecule):
    """
    Calculates the dynamic force between two dynamic bodies, assumed to be atoms affected by the Coulomb force
    :param db1:
    :param db2:
    :return:
    """
    distance_vector = db2.position - db1.position
    try:
        force = units.c_const * db1.charge * db2.charge / (distance_vector.map ** 2)
    except ZeroDivisionError:
        return Vector3(0, 0, 0)
    return distance_vector.as_unit() * force


def coulombic_acceleration(db1: Molecule, db2: Molecule):
    force = coulomb_force(db1, db2)
    return force / db1.mass

