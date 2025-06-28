from sympy import symbols, diff, sin
from energy import potential
from solver import find_roots,verify_roots
from visualize_particles import visualize_particles
from lenlen import coefficientgen

lam_da = 286.06e-6
z = -7603
k = -2215
nums = 7
#set up potential object with constants
p = potential(lam_da, z, k)
l = symbols("l")
if nums > 7:
    print("ERROR: this code only works for n<8")
#get the length coefficients of all the possible combinations of particles, so they can be expressed
#as al, l being the distance between any adjacent 2
if nums < 6:
    lengths, c = coefficientgen(nums)
    r = l/c
    lengths = lengths/c
    #construct the energy equation by adding the confinement term
    exp = nums * p.confinement(r)
    #add terms for each energy interaction between particles
    for i in lengths:
        exp += p.interaction(i*l)
    
if nums == 7:
    lengths, c = coefficientgen(6)
    r = l/c
    lengths = lengths/c
    #when nums=7, one particle is at the center of a hexagon
    exp = 6 * p.confinement(r)
    #add terms for each energy interaction between particles
    for i in lengths:
        exp += p.interaction(i*l)
    #adding the interaction potential of the center particle
    exp += p.interaction(r)*6
if nums == 6:
    lengths, c = coefficientgen(5)
    r = l/c
    lengths = lengths/c
    #when nums=7, one particle is at the center of a hexagon
    exp = 5 * p.confinement(r)
    #add terms for each energy interaction between particles
    for i in lengths:
        exp += p.interaction(i*l)
    #adding the interaction potential of the center particle
    exp += p.interaction(r)*5


print(exp)

# take the derivative
dff = diff(exp, l)
diff2 = diff(dff,l)
#find roots
roots = find_roots(dff, 0.0001, 3e-2, 10000)
#filter out maxxes and horizontal tangents
for i in roots:
    if(diff2.subs(l,i).evalf()<=0):
        roots.remove(i)
        i=roots[0]
print(roots)
