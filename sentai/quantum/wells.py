from sentai import units


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



