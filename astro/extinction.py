import math


"""
Functions to process interstellar medium dust and gas extinction.
"""


def apparent_magnitude(abs_mag=0, extinction=0, dist=1):
    """
    Calculates the apparent magnitude of an object a given distance away, with a known
    absolute magnitude.
    :param abs_mag: Absolute magnitude (in mag)
    :param extinction: Extinction value (in mag)
    :param dist: Distance to the object (in pc)
    :return: The apparent magnitude (in mag)
    """
    try:
        app_mag = (5 * math.log(dist, 10)) - 5 + extinction + abs_mag
        return app_mag
    except:
        print("Error. Check your inputs.")
        return 0


def mean_free_path(sigma, n):
    """
    Calculates the mean free path for a given cross section and number density.
    :param sigma: Inverse Cubic Units
    :param n: Squared Units
    :return: Mean Free path in given units
    """
    return 1 / (sigma * n)
