from sentai import units
from sentai.dynamics.DynamicBody import *
from sentai.simulation import nbodysim
from sentai.plotting import plots

db1 = DynamicBody(Vector3(0, 0, 0), Vector3(0, 0, 0), units.m_sun)
db2 = DynamicBody(Vector3(units.dist_earth, 0, 0), Vector3(0, 30 * units.km, 0), units.m_earth)
db3 = DynamicBody(Vector3(units.dist_jupiter, 0, 0), Vector3(0, 10 * units.km, 0), units.m_jupiter)

# positions = nbodysim.celestial_body_sim([db1, db2], 1 * units.day, 10 * units.yr)
positions = nbodysim.celestial_body_sim([db1, db2, db3], 1 * units.day, 10 * units.yr)

plots.n_body_plot(positions, convert_to=units.au)
