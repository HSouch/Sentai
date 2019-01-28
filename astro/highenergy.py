
def photoelectric_absorption(energy):
    """
    Returns the photoelectric absorption for a given energy
    :param energy: Must be in units of keV
    :return:
    """
    return 2e-22 * (energy ** (-8 / 3))
