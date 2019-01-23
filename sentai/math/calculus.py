def simpson(f, a, b, n):
    """
    Returns the integral for a function from a to b using Simpson's Rule. User-set number of steps n.
    :param f: Function to be integrated over.
    :param a: Left Bound
    :param b: Right Bound
    :param n: Number of steps between and a and b. Must be an even number.
    :return:
    """
    if n % 2 != 0:
        n += 1

    h = (b - a) / n
    total_sum = f(a) + f(b)
    for i in range(1, n):
        x_i = a + (i * h)
        mul = 2 if (i % 2) == 0 else 4  # Multiplier
        total_sum += (mul * f(x_i))

    return (h / 3) * total_sum


def trapezoidal(f, a, b, n):
    """
    Returns the integral for a function from a to b using Simpson's Rule. User-set number of steps n.
    :param f: Function to be integrated over.
    :param a: Left Bound
    :param b: Right Bound
    :param n: Number of steps between and a and b. Must be an even number.
    :return:
    """
    h = (b - a) / n
    total_sum = f(a) + f(b)
    for i in range(1, n):
        x_i = a + (i * h)
        total_sum += (2 * f(x_i))

    return (h / 2) * total_sum


def derivative(func, x, delta=10e-6):
    """
    Returns the derivative of a function at a given x value. Delta is adjustable but set to a reasonable starting
    amount
    """
    return (func(x + delta) - func(x)) / delta
