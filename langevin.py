import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt
from diffeq import euler_maruyama

# Constants
k_B = 1.38e-23        # Boltzmann 
T = 300               # Temperature
P = 101325            # Pressure 
particle_radius = 250e-9  # Particle radius 
particle_density = 1000   # Particle density 
particle_volume = (4/3) * np.pi * particle_radius**3
particle_mass = particle_density * particle_volume  # Particle mass 
gas_viscosity = 1.8e-5    # Gas viscosity 
particle_diameter = 2 * particle_radius # Particle diameter 
gas_molecule_diameter = 0.37e-9 # Approximate diameter of air molecule
g = 9.81 

#Knudsen number
mean_free_path = (k_B * T) / (np.sqrt(2) * np.pi * gas_molecule_diameter**2 * P)
Kn = mean_free_path / particle_radius

# Calculate friction scalar factor
cunningham = 2.25*(0.4 + Kn * np.exp(-1.1 / Kn))
f_stokes = 6 * np.pi * gas_viscosity * particle_radius
f = f_stokes / cunningham

"""
define the differential equation, representing the vertical component 
of the brownian force with a normally distributed random number and 
standard deviation as cacluated below
"""

def dvdt(v,t):
    drift = g - (f / particle_mass) * v
    diffusion = np.sqrt(2 * f * k_B * T) / particle_mass
    return (drift, diffusion)

#define the initial velocity as a normally distributed random number with thermal equilibrium with the surrounding gas
v0 = np.random.normal(loc=0, scale=np.sqrt(k_B * T / particle_mass))
val = []
for i in range(0,100):
    t, v = euler_maruyama(dvdt, v0, t_span=(0, 2), dt=1e-6)
    x = cumulative_trapezoid(v, t, initial=0)
    val.append(x[-1])
plt.hist(val, bins=10)
plt.xlabel("Distance reached after 2 seconds")
plt.ylabel("Number of Trials")
plt.title("Histogram of Trials")
plt.show()

# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# ax1.plot(t, v)
# ax1.set_title("Particle Velocity vs. Time")
# ax1.set_ylabel("Velocity (m/s)")
# ax1.grid(True)

# ax2.plot(t, x)
# ax2.set_title("Particle Position vs. Time")
# ax2.set_xlabel("Time (s)")
# ax2.set_ylabel("Position (m)")
# ax2.grid(True)

# plt.tight_layout()
# plt.show()
