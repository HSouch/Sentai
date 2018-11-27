from sentai.dynamics.DynamicBody import *
from sentai.plotting import plotting
import numpy as np

db1 = DynamicBody(Vector3(0, 0, 0), Vector3(0, 0, 0), units.m_sun)
db2 = DynamicBody(Vector3(units.dist_earth, 0, 0), Vector3(0, 30 * units.km, 0), units.m_earth)
db3 = DynamicBody(Vector3(units.dist_jupiter, 0, 0), Vector3(0, 10 * units.km, 0), units.m_jupiter)


# positions = nbodysim.celestial_body_sim([db1, db2], 1 * units.day, 10 * units.yr)

# for x in range(0, 1):
#     bodies = random_gen.generate_random_bodies(10000, 5 * units.au, 40 * units.km, 1 * units.m_earth, 4 * units.m_sun)
#     nbodysim.advanced_celestial_body_sim(bodies, 1, 1)

ls = [.663, .939, 1.228, 1.559]
err_ls = [0.005, 0.005, 0.005, 0.01]
ts = [16.92, 19.95, 22.69, 25.62]
err_ts = [0.5, 0.5, 0.5, 0.5]


def calc_g(l, t):
    return (4 * (math.pi ** 2) * l) / (t ** 2)

gs = []
for ind in range(0, len(ls)):
    gs.append(calc_g(ls[ind], ts[ind] / 10))


for ind in range(0, len(ls)):
    ts[ind] /= 10
    err_ts[ind] /= 10

# plotting.gen_plot(ts, ls, err_y=err_ls, err_x=err_ts, fit=True, show_slope=True, slope_label="g", show_plot=True)


def calc_err_g(t, l, err_l, err_t):
    comp_1 = (((4 * (units.pi ** 2)) / (t ** 2)) ** 2) * (err_l ** 2)
    comp_2 = (((8 * (units.pi ** 2) * l) / (t ** 3)) ** 2) * (err_t ** 2)

    return math.sqrt(comp_1 + comp_2)

err_gs = []
for ind in range(0, len(ts)):
    err_gs.append((calc_err_g(ts[ind], ls[ind], err_ls[ind], err_ts[ind])))

print(np.mean(err_gs))
