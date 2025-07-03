import random
import numpy as np
from energy import potential
from distancemat import compute_distance_matrix
class EnergyModel:
    def __init__(self,num,space_lengthcm,lamb_da,z,k):
        self.p = potential(lamb_da,z,k)
        self.num = num
        self.space_lengthm = space_lengthcm/100

    def init_space(self):
        return np.random.uniform(-self.space_lengthm/2,self.space_lengthm/2,(self.num,2))
    def instant_energy(self,coords):
        deltas = compute_distance_matrix(coords)
        U = 0
        for d in deltas:
            U += self.p.interaction(d)
        for c in coords:
            U += self.p.confinement(np.sqrt(c[0]**2 +c[1]**2))
        return U
    # def unflatten(self,mat):
    #     if (len(mat)%2 != 0):
    #         raise ValueError("The array must have an even amount of entries.")
    #     y=[]
    #     x=[]
    #     for i in range(0,len(mat)):
    #         if (i%2 != 0):
    #             y.append(mat[i])
    #         else:
    #             x.append(mat[i])
    #     arr = np.column_stack((x,y))
    #     return arr.tolist()
    """
    Need a way to mimimize the U that instant_energy returns with
    respect to all x and y coords of each particle.
    
    """
# lamb_da = 286.06e-6
# z = -7603
# k = -2215
# system = energy_model(2,18,lamb_da,z,k)
# a = 0.0009320499869210618
# coords = [[a/2,0],[-a/2,0]]
# print(system.instant_energy(coords))