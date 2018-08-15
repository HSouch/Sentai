from sentai import units
from sentai.dynamics.DynamicBody import *
from sentai.simulation import nbodysim


db1 = DynamicBody(Vector3(0, 0, 0), Vector3(0, 0, 0), units.m_sun)
db2 = DynamicBody(Vector3(1 * units.au, 0, 0), Vector3(0, 30 * units.km, 0), units.m_earth)

nbodysim.celestial_body_sim([db1, db2], 1 * units.day, 10 * units.day)