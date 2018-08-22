from sentai import units
from sentai.dynamics.DynamicBody import *
from sentai.simulation import nbodysim, random_gen
from sentai.plotting import plots

db1 = DynamicBody(Vector3(0, 0, 0), Vector3(0, 0, 0), units.m_sun)
db2 = DynamicBody(Vector3(units.dist_earth, 0, 0), Vector3(0, 30 * units.km, 0), units.m_earth)
db3 = DynamicBody(Vector3(units.dist_jupiter, 0, 0), Vector3(0, 10 * units.km, 0), units.m_jupiter)


# positions = nbodysim.celestial_body_sim([db1, db2], 1 * units.day, 10 * units.yr)

for x in range(0, 1):
    bodies = random_gen.generate_random_bodies(10000, 5 * units.au, 40 * units.km, 1 * units.m_earth, 4 * units.m_sun)
    nbodysim.advanced_celestial_body_sim(bodies, 1, 1)


# plots.n_body_plot(positions, convert_to=units.au)

