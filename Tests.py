from sentai.dynamics.DynamicBody import *
from sentai.plotting import plotting

db1 = DynamicBody(Vector3(0, 0, 0), Vector3(0, 0, 0), units.m_sun)
db2 = DynamicBody(Vector3(units.dist_earth, 0, 0), Vector3(0, 30 * units.km, 0), units.m_earth)
db3 = DynamicBody(Vector3(units.dist_jupiter, 0, 0), Vector3(0, 10 * units.km, 0), units.m_jupiter)


# positions = nbodysim.celestial_body_sim([db1, db2], 1 * units.day, 10 * units.yr)

# for x in range(0, 1):
#     bodies = random_gen.generate_random_bodies(10000, 5 * units.au, 40 * units.km, 1 * units.m_earth, 4 * units.m_sun)
#     nbodysim.advanced_celestial_body_sim(bodies, 1, 1)

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 20, 15, 32, 23, 18, 9, 5]
err = [3, 2, 1, 2, 3, 3, 1, 1]


plotting.gen_plot(x, y, err=err, show_plot=True, xlabel="test_x", ylabel="test_y", save_plot=True)
