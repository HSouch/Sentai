from sentai.units import pi


def sphere_volume(r):
    """ Returns the volume of a sphere of radius r units"""
    return (4 / 3) * pi * (r ** 3)


def sphere_surface_area(r):
    """ Returns the surface area of a sphere of radius r units"""
    return 4 * pi * (r ** 2)


def cylinder_volume(r, h):
    """ Returns the volume of a cylinder of radius r and height h"""
    return (pi * r ** 2) * h


def cylinder_surface_area(r, h):
    """ Returns the surface area of a cylinder of radius r and height h"""

    return (2 * pi * r * h) + (2 * pi * r ** 2)


def cone_volume(r, h):
    """ Returns the volume of a cone of radius r and height h"""
    return pi * (r ** 2) * (h / 3)
