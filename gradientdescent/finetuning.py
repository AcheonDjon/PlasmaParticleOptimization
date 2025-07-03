from gradient import grad_run
import numpy as np
from energymodel import EnergyModel
lamb_da = 286.06e-6
z = -7603
k = -2215
#params to be tuned
step = 0.5e9
tolerance = 1e-16
epsilon =1e-16
ivector = np.array([step,tolerance,epsilon])
system = EnergyModel(3,18,lamb_da,z,k)
coords = system.init_space()
def adjacent_distances(coords):
    diffs = coords[1:] - coords[:-1]           # shape: (n-1, 2)
    distances = np.linalg.norm(diffs, axis=1)  # shape: (n-1,)
    return distances
def error(ivector):
    mat = grad_run(coords,ivector[0],ivector[1],ivector[2])
    nearest_neighbor = adjacent_distances(mat)
    erf = nearest_neighbor[0]-nearest_neighbor[1]
    return erf
def finite_difference(f,x, epsilon):
    flat = x
    grad = [0]*len(flat)
    for i in range(len(flat)):
        xplus = flat.copy()
        xminus = flat.copy()
        xplus[i] += epsilon
        xminus[i] -= epsilon
        grad[i] = (f(xplus)-f(xminus))/(epsilon*2)
    return np.array(grad)
U =[]
gradient_norm =1
while gradient_norm>1e-5:
    #calculate the gradient of the potential energy of the coordinates
    u = error(ivector)
    U.append(u)
    gradv = finite_difference(error, ivector,1e-8)
    #find the magnitude of the vector
    gradient_norm = np.linalg.norm(gradv)
    #loop through every coordinate and adjust it according to the gradient
    ivector -= (gradv*step)
    # arrange the adjusted flat_c back into a 2d array and put it back into coords