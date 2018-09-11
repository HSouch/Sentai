from sentai import units
import math


"""
Functions to process interstellar medium dust and gas extinction.
"""


def calc_apparent_magnitude(abs_mag=0, extinction=0, dist=1):
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


print(calc_apparent_magnitude(-1.3, 1.1, 700))
