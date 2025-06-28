import streamlit as st
from sympy import symbols, diff
from energy import potential
from solver import find_roots
from visualize_particles import visualize_particles
from lenlen import coefficientgen
import matplotlib.pyplot as plt

st.title("Plasma Particle Optimization Visualizer")

st.sidebar.header("Input Parameters")
lam_da = st.sidebar.number_input("Lambda (lam_da)", value=300 * 10e-6, format="%e")
z = st.sidebar.number_input("z", value=-7000)
k = st.sidebar.number_input("k", value=-1000)
nums = st.sidebar.number_input("Number of particles (nums)", min_value=2, max_value=20, value=7)

if st.button("Compute and Visualize"):
    p = potential(lam_da, z, k)
    l = symbols("l")
    lengths, c = coefficientgen(nums)
    r = l / c
    lengths = lengths / c
    exp = nums * p.confinement(r)
    for i in lengths:
        exp += p.interaction(i * l)
    dff = diff(exp, l)
    diff2 = diff(dff, l)
    roots = find_roots(dff, 0.0001, 3e-3, 10000)
    # Filter out maxima and horizontal tangents
    roots = [i for i in roots if diff2.subs(l, i).evalf() > 0]
    st.write(f"Roots (possible equilibrium distances): {roots}")
    if roots:
        try:
            l_val = float(roots[0])
            fig, ax = plt.subplots()
            visualize_particles(nums, l_val, ax=ax)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Visualization failed: {e}")
    else:
        st.warning("No valid roots found.")
