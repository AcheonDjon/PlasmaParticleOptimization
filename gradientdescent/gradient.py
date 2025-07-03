
from energymodel import EnergyModel
import matplotlib.pyplot as plt
import numpy as np

lamb_da = 286.06e-6
z = -7603
k = -2215
system = EnergyModel(28,18,lamb_da,z,k)
coords = system.init_space()
def finite_difference(f,x, epsilon):
    flat = x.reshape(-1)
    grad = [0]*len(flat)
    for i in range(len(flat)):
        xplus = flat.copy()
        xminus = flat.copy()
        xplus[i] += epsilon
        xminus[i] -= epsilon
        xplus = xplus.reshape(-1,2)
        xminus = xminus.reshape(-1,2)
        grad[i] = (f(xplus)-f(xminus))/(epsilon*2)
    return np.array(grad)

# mat = [[6,7],[8,4],[2,3]]
# def k(i):
#     return i[0][0]**2 + i[0][1]**2 + i[1][0]**2 + i[1][1]**2 + i[2][0]**2 + i[2][1]**2
# print(finite_difference(k,mat))

def grad_run(coords,step,tolerance,epsilon=1e-16):
    U =[]
    gradient_norm =1
    while gradient_norm>tolerance:
    
        #calculate the gradient of the potential energy of the coordinates
        u = system.instant_energy(coords)
        U.append(u)
        gradv = finite_difference(system.instant_energy, coords,epsilon)
        #find the magnitude of the vector
        gradient_norm = np.linalg.norm(gradv)
        #flatten coords out
        flat_c = coords.reshape(-1)
        #loop through every coordinate and adjust it according to the gradient
        flat_c -= (gradv*step)
        # arrange the adjusted flat_c back into a 2d array and put it back into coords
        coords = flat_c.reshape(-1,2)
    return coords #, U
step = 0.5e9
# print(coords == system.unflatten(flat_c))
print(f"Initial coordinates: {coords}")
tolerance = 1e-16
elipson =1e-16
grad_run(coords,step,tolerance,elipson)
print(f"Final coordinates: {coords}")
fc = coords
# fc =np.array([[0,2],[2,0],[-2,0],[0,-2]])
plt.scatter(coords[:,0],coords[:,1])
plt.title("Equilibrium Position of Particles")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
# fig, (ax1,ax2) = plt.subplots(2, 1, figsize=(12, 12), sharex=False)
# ax1.scatter(fc[:,0]*100,fc[:,1]*100)
# ax1.set_title("Equilibrium Location of Particles")
# ax1.set_xlabel("X(cm)")
# ax1.set_ylabel("Y(cm)")
# ax1.grid(True)
# ax2.plot(np.arange(len(U)),U )
# ax2.set_title("Energy History")
# ax2.set_xlabel("Iterations")
# ax2.set_ylabel("Energy(Joules)")
# plt.tight_layout()
# plt.show()
