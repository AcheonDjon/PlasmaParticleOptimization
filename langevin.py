import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
# Constants
k_B = 1.38e-23        # Boltzmann constant (J/K)
T = 300               # Temperature (K)
P = 101325            # Pressure (Pa)
particle_radius = 250e-9  # Particle radius (m)
particle_mass = 1000 * 1.04e-6  # Particle mass (kg)
gas_viscosity = 1.8e-5    # Gas viscosity (Pa.s)
particle_diameter = 500e-9 # Particle diameter (m)
pi = np.pi

# Calculate the Knudsen number
Kn = (k_B * T) / (np.sqrt(2) * pi * (particle_diameter)**2 * P * particle_radius)

# Calculate friction parameters
n = 6 * pi * gas_viscosity * particle_radius
s = 1.1 / Kn
d = (1 + 1.250 * (0.4 + Kn * np.exp(s)))

# Calculate scalar friction tensor
f = n / d

# Time step for Brownian force calculation
deltat = 0.01

# Calculate the standard deviation of the Brownian force
std = np.sqrt((6 * f * T * k_B) / deltat)
"""
define the differential equation, representing the vertical component 
of the brownian force with a normally distributed random number and 
standard deviation as cacluated above
"""
def dvdt(t,v):
    return 9.81 - (f/particle_mass)*v + np.random.normal(loc=0, scale=std)
#define the initial velocity as a normally distributed random number with thermal equilibrium with the surrounding gas
v0 = [np.random.normal(loc=0,scale = np.sqrt((1.38e-23*300)/particle_mass))]
t_span = (0,10000)
#solve the equation numerically
solution = solve_ivp(dvdt,t_span,v0, dense_output=True)
t = np.linspace(0,10000,100)
y = solution.sol(t)
