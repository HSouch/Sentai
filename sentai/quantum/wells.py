from sentai import units
import math


def get_energy_state(n=0, length=0, mass=0, convert_to=1):
    """
    Returns the energy levels for a particle of mass m, inside an infinite potential well with given length. Will
    convert to a given set of units if specified, otherwise will return SI units.
    :param n:
    :param length:
    :param mass:
    :param convert_to:
    :return:
    """
    if mass == 0 or length == 0:
        print("Input error, check your values")
        return None
    energy_level = ((n ** 2) * units.pi * (units.h_bar ** 2)) / (2 * mass * (length ** 2))
    return energy_level / convert_to


def get_num_of_states(length=0, v=0, mass=0):
    """
    Returns the number of possible states within a finite potential well.
    Uses the equation N = int(sqrt(v_0 / E_0) + 1), where
        E_0 = (pi^2 * h_bar^2) / 8mL^2
    :param length:
    :param v:
    :param mass:
    :return:
    """
    if mass == 0 or length == 0 or v == 0:
        print("Input error, check your values")
        return None
    e_naught = (math.pi ** 2 * units.h_bar ** 2) / (8 * mass * length ** 2)
    states = int(math.sqrt(v / e_naught) + 1)
    return states
