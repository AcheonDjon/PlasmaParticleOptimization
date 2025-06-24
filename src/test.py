from energy import potential
from sympy import symbols, diff
from lenlen import coefficientgen

lam_da = 300 * 10e-6
z = -7000
k = -1000
nums = 2
p = potential(lam_da, z, k)
l = symbols("l")


lengths, c = coefficientgen(nums)
r = l/c
lengths = lengths/c
exp = nums * p.confinement(r)
print(lengths)
for i in lengths:
    exp += p.interaction(i*l)


# take the derivative
dff = diff(exp, l)
print(dff.subs(l,4000000).evalf())
