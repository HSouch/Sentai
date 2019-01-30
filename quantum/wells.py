from sentai import units
from matplotlib import pyplot as plt
from numpy import floor, pi, sqrt, arange, sin, cos

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
    e_naught = (pi ** 2 * units.h_bar ** 2) / (8 * mass * length ** 2)
    states = sqrt(v / e_naught) + 1
    return states, int(states)


def simple_get_num_of_states(length=0, mass=0, v=0):
    if mass == 0 or length == 0 or v == 0:
        print("Input error, check your values")
        return None
    k = get_k(length=length, mass=mass, v=v)
    return floor((2 * k / units.pi) + 1)


def build_finite_energy_function(mass=0, v=0, length=0):
    if mass == 0 or length == 0 or v == 0:
        print("Input error, check your values")
        return None
    k = get_k(mass=mass, v=v, length=length)
    xs = arange(0, 5, 0.0001)
    ys = []
    for x in range(0, len(xs)):
        ys.append(get_finite_energy_function_indval(xs[x], k))
    plt.xticks(arange(0,6, step=0.1))
    plt.plot(xs, ys)
    plt.plot(xs, 0 * xs)
    plt.grid()
    plt.show()
    roots = [1.31, 2.00, 3.85, 4.94]  # Roots found graphically from the corresponding plot output.
    for root in roots:  # Get energy values for each root
        a = root / length
        energy = (a ** 2 * units.h_bar ** 2) / (2 * mass)
        print(root, a, energy, energy / units.electron_volt)


def get_finite_energy_function_indval(chi, k):
    # Returns an individual value for the corresponding f(chi, k) function.
    val = (k ** 2 - (2 * chi ** 2)) * sin(2 * chi)
    val += (2 * chi * sqrt(abs(k ** 2 - chi ** 2)) * cos(2 * chi))
    return val


def get_k(mass=0, v=0, length=0):
    if mass == 0 or length == 0 or v == 0:
        print("Input error, check your values")
        return None
    k = sqrt((2 * mass * v * (length ** 2)) / (units.h_bar ** 2))
    return k