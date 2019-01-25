from sentai.astro import *
# positions = nbodysim.celestial_body_sim([db1, db2], 1 * units.day, 10 * units.yr)

# for x in range(0, 1):
#     bodies = random_gen.generate_random_bodies(10000, 5 * units.au, 40 * units.km, 1 * units.m_earth, 4 * units.m_sun)
#     nbodysim.advanced_celestial_body_sim(bodies, 1, 1)

energies = [0.02, 0.2, 2, 20]

for e in energies:
    print(e, photoelectric_absorption(e), mean_free_path(photoelectric_absorption(e), 1),
          mean_free_path(photoelectric_absorption(e), 1) * units.cm / units.pc)