from sympy import symbols, diff, sin
from energy import potential
from solver import find_roots,verify_roots
from visualize_particles import visualize_particles
from lenlen import coefficientgen

lam_da = 300 * 10e-6
z = -7000
k = -1000
nums = 7
#set up potential object with constants
p = potential(lam_da, z, k)
l = symbols("l")

#get the length coefficients of all the possible combinations of particles, so they can be expressed
#as al, l being the distance between any adjacent 2
lengths, c = coefficientgen(nums)
r = l/c
lengths = lengths/c
#construct the energy equation by adding the confinement term
exp = nums * p.confinement(r)
#add terms for each energy interaction between particles
for i in lengths:
    exp += p.interaction(i*l)

print(exp)

# take the derivative
dff = diff(exp, l)
diff2 = diff(dff,l)
#find roots
roots = find_roots(dff, 0.0001, 3e-3, 10000)
#filter out maxxes and horizontal ta
for i in roots:
    if(diff2.subs(l,i).evalf()<=0):
        roots.remove(i)
print(roots)
# # Visualize the arrangement for the first root (if any)
# if roots:
#     try:
#         l_val = float(roots[0])
#         visualize_particles(nums, l_val)
#     except Exception as e:
#         print(f"Visualization failed: {e}")