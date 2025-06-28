import random
import numpy as np
from src.energy import potential
from src.distancemat import compute_distance_matrix
from sympy import symbols
class energy_model:
    def __init__(self,num,space_lengthcm,lamb_da,z,k):
        self.p = potential(lamb_da,z,k)
        self.num = num
        self.space_lengthcm = space_lengthcm

    def init_space(self):
        coords=[]
        for i in range(0,self.num):
            x = random.uniform(-self.space_lengthcm/2,self.space_lengthcm/2)
            y = random.uniform(-self.space_lengthcm/2,self.space_lengthcm/2)
            pair = [x,y]
            coords.append(pair)
        return coords
    def instant_energy(self,coords):
        deltas = compute_distance_matrix(coords)
        U = 0
        for d in deltas:
            U += self.p.interaction(d)
        for c in coords:
            U += self.p.confinement(np.sqrt(c[0]**2 +c[1]**2))
        return U
    def unflatten(self,mat):
        if (len(mat)%2 != 0):
            raise ValueError("The array must have an even amount of entries.")
        y=[]
        x=[]
        for i in range(0,len(mat)):
            if (i%2 != 0):
                y.append(mat[i])
            else:
                x.append(mat[i])
        arr = np.column_stack((x,y))
        return arr.tolist()
    """
    Need a way to mimimize the U that instant_energy returns with
    respect to all x and y coords of each particle.
    
    """