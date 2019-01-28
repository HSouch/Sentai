"""
Units for sentai and related applications. All units are derived from SI units.
"""

r_e = 10e-16                    # Rounding error in Python
rounding_error = r_e            # Rounding Error in Python

# Constants
p_length = 1.616229e-35         # Planck Length (in m)
p_mass = 2.176e-8               # Planck Mass (in kg)
p_time = 5.3912e-44             # Planck time (in s)

pi = 3.141592653589             # Pi (To 12 digits)
c = 2.99782e8                   # Speed of light (m/s)
g = 6.67408e-11                 # Gravitational Constant (m^3 * kg^-1 * s^-2)
h = 6.6261e-34                  # Planck Constant (J * s)
h_bar = 1.0546e-34              # Reduced Planck Constant (J * s)

k = 8.987552e9                  # Coulomb's Constant (1/(4 * pi * epsilon_naught))
c_const = 8.987552e9            # Coulomb's Constant (1/(4 * pi * epsilon_naught))

sb = 5.670367e-8                # Stefan-Boltzmann Constant
stef_boltz = sb                # Stefan-Boltzmann Constant

e_fund = 1.6022e-19             # Fundamental Charge
epsilon_naught = 8.85418e-12    # Vacuum Permittivity
electron_volt = 1.602e-19       # Electron Volt
eV = 1.602e-19                  # Electron Volt
MeV = eV * 1e6


# Fundamental Units of Mass
m_electron = 9.109384e-31       # Mass of Electron
m_proton = 1.672622e-27         # Mass of Proton
m_neutron = 1.674927e-27        # Mass of Neutron


# Metric Units of Mass
mg = 1e-6                       # Milligram
gram = 1e-3                     # Gram
tonne = 1000                    # Metric Tonne


# Distances
ang = 1e-10                     # Angstrom
nm = 1e-9                       # Nanometre
mm = 1e-3                       # Millimetre
cm = 1e-2                       # Centimetre
dm = 1e-1                       # Decimetre
km = 1000                       # Kilometre
au = 149597870700               # Astronomical Unit
ly = 9.4607e15                  # Light Year
pc = 3.0857e16                  # Parsec


# Times
minute = 60                     # Minute
hour = 3600                     # Hour
day = 86400                     # Day
yr = 3.154e+7                   # Year


# Celestial Masses
m_sun = 1.9885e30               # Solar Mass
m_mercury = 3.30e23             # Mass of Mercury
m_venus = 4.87e24               # Mass of Venus
m_earth = 5.97e24               # Mass of Earth
m_moon = 7.3e22                 # Mass of Earth's moon
m_mars = 6.42e23                # Mass of Mars
m_jupiter = 1.898e27            # Mass of Jupiter
m_saturn = 5.68e26              # Mass of Saturn
m_uranus = 8.68e25              # Mass of Uranus
m_neptune = 1.02e26             # Mass of Neptune
m_pluto = 1.46e22               # Mass of Pluto


# Celestial Radii
r_sun = 6.955e8                 # Solar Radius
r_earth = 6.3781e6              # Earth Radius


# Celestial Distances (from sun)
dist_mercury = 5.79e10
dist_venus = 1.082e11
dist_earth = 1.496e11
dist_mars = 2.279e11
dist_jupiter = 7.786e11
dist_saturn = 1.4335e12
dist_uranus = 2.8725e12
dist_neptune = 4.4951e12
dist_pluto=5.9064e12


# Imperial Units
inch = .0254                    # Inch
ft = 0.3048                     # Foot
yd = 0.9144                     # Yard
mile = 1609.3                   # Mile

oz = 0.2835                     # Ounce
lb = 0.4536                     # Pound
st = 6.3503                     # Stone


# Atomic Mass Units
amu = 1.660539e-27              # Atomic Mass Unit
m_H = 1.007 * amu               # Hydrogen
m_He = 4.002 * amu              # Helium
m_Li = 6.938 * amu              # Lithium
m_Be = 9.012 * amu              # Beryllium
m_B = 10.806 * amu              # Boron
m_C = 12.0096 * amu             # Carbon
m_N = 14.006 * amu              # Nitrogen
m_O = 15.999 * amu              # Oxygen
m_F = 18.998 * amu              # Florine
m_Ne = 20.1797 * amu            # Neon
m_Na = 22.989 * amu             # Sodium
m_Mg = 24.304 * amu             # Magnesium
m_Al = 26.981 * amu             # Aluminium
m_Si = 28.084 * amu             # Silicon
m_P = 30.973 * amu              # Phosphorous
m_S = 32.059 * amu              # Sulfur
m_Cl = 35.446 * amu             # Chlorine
m_Ar = 39.948 * amu             # Argon
m_K = 39.0983 * amu             # Potassium
m_Ca = 40.078 * amu             # Calcium
m_Sc = 44.955 * amu             # Scandium
m_Ti = 47.867 * amu             # Titanium
m_Va = 50.9415 * amu            # Vanadium
m_Cr = 51.9961 * amu            # Chromium
m_Mn = 54.938 * amu             # Manganese
m_Fe = 55.845 * amu             # Iron
m_Co = 58.933 * amu             # Cobalt
m_Ni = 58.6934 * amu            # Nickel
m_Cu = 63.546 * amu             # Copper
m_Zn = 65.38 * amu              # Zinc
m_Ga = 69.723 * amu             # Gallium
m_Ge = 72.630 * amu             # Germanium
m_As = 74.921 * amu             # Arsenic
m_Se = 78.971 * amu             # Selenium
m_Br = 79.901 * amu             # Bromine
m_Kr = 83.798 * amu             # Krypton
m_Rb = 85.4678 * amu            # Rubidium
m_Sr = 87.62 * amu              # Strontium
m_Y = 88.905 * amu              # Yttrium
m_Zr = 91.224 * amu             # Zirconium
m_Nb = 92.906 * amu             # Niobium
m_Mo = 95.95 * amu              # Molybdenum
m_Ru = 101.07 * amu             # Ruthenium
m_Rh = 102.905 * amu            # Rhodium
m_Pd = 106.42 * amu             # Palladium
m_Ag = 107.8682 * amu           # Silver
m_Cd = 112.414 * amu            # Cadmium
m_In = 114.818 * amu            # Indium
m_Sn = 118.710 * amu            # Tin
m_Sb = 121.760 * amu            # Antimony
m_Te = 127.60 * amu             # Tellurium
m_I = 126.904 * amu             # Iodine
m_Xe = 131.293 * amu            # Xenon
m_Sc = 132.905 * amu            # Caesium
m_Ba = 137.327 * amu            # Barium
m_Lu = 138.905 * amu            # Lutetium
