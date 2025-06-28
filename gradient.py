import torch
from energymodel import energy_model
import matplotlib.pyplot as plt
import numpy as np
lamb_da = 286.06e-6
z = -7603
k = -2215
system = energy_model(2,18,lamb_da,z,k)
coords = system.init_space()
def finite_difference(f,x, epsilon = 1e-5):
    flat = [item for sublist in x for item in sublist]
    grad = [0]*len(flat)
    for i in range(len(flat)):
        xplus = flat.copy()
        xminus = flat.copy()
        xplus[i] += epsilon
        xminus[i] -= epsilon
        xplus = system.unflatten((xplus))
        xminus = system.unflatten((xminus))
        grad[i] = (f(xplus)-f(xminus))/(epsilon*2)
    return grad
step = 0.1
flat_c = [item for sublist in coords for item in sublist]

for b in range(1000):
    gradv = finite_difference(system.instant_energy, coords)
    for i in range(len(gradv)):
       flat_c[i] = flat_c[i]- step*gradv[i]

fc = np.array(system.unflatten(flat_c))
# fc =np.array([[0,2],[2,0],[-2,0],[0,-2]])
plt.scatter(fc[:,0],fc[:,1])
plt.title("Equilibrium Location of Particles")
plt.xlabel("X(cm)")
plt.ylabel("Y(cm)")
plt.grid(True)
plt.show()
