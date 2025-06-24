from sympy import E,pi,sin,cos
echarge = 1.602e-19
elipson = 8.85e-12

class potential:
    def __init__(self,lam_da, z, k):
        self.lam_da = lam_da
        self.z = z
        self.k = k
        self.c = (z**2*echarge**2)/(4*pi*elipson)

    def interaction(self, l):
       return (self.c/l)*E**(-l/self.lam_da)
    
    def confinement(self, r):
        return self.k*(self.z*r**2)*(echarge)