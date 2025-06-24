from sympy import symbols, diff, sin
from energy import potential
from solver import find_roots
from visualize_particles import visualize_particles

lam_da = 300 * 10e-6
z = 7000
k = -1000
nums = 2
p = potential(lam_da, z, k)
l = symbols("l")

if nums == 2:
    r = l / 2
# if nums == 3:
#     r =
# if nums == 4:
#     d
# if nums == 5:
#     d
# if nums == 6:
#     d
# if nums == 7:
#     d
exp = p.interaction(l) + nums * p.confinement(r)
print(exp)

# take the derivative
dff = diff(exp, l)

roots = find_roots(dff, 1e4, 2e3, 1000000)
print(roots)

# # Visualize the arrangement for the first root (if any)
# if roots:
#     try:
#         l_val = float(roots[0])
#         visualize_particles(nums, l_val)
#     except Exception as e:
#         print(f"Visualization failed: {e}")