import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, E, pi, sin, cos
from scipy.optimize import brentq
import sympy as sp

# Constants
echarge = 1.602e-19
elipson = 8.85e-12

class potential:
    def __init__(self, lam_da, z, k):
        self.lam_da = lam_da
        self.z = z
        self.k = k
        self.c = (z**2*echarge**2)/(4*pi*elipson)

    def interaction(self, l):
        return (self.c/l)*E**(-l/self.lam_da)
    
    def confinement(self, r):
        return self.k*(self.z*r**2)*(echarge)

def compute_distance_matrix(points):
    """Compute pairwise distances and return unique distances."""
    points = np.array(points)
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    distance_matrix = np.linalg.norm(diff, axis=2)
    distance_matrix = distance_matrix.flatten().tolist()
    half = len(distance_matrix)//2
    if len(distance_matrix)%2 == 0:
        distance_matrix = distance_matrix[:half]
    else:
        distance_matrix = distance_matrix[:half+1]
    cleaned = [x for x in distance_matrix if x != 0]
    return cleaned

def generate_circle_points(n, radius=1, center=(0, 0), start_angle=0):
    """Generate n equally spaced points on circle perimeter."""
    if n < 1:
        raise ValueError("Number of points must be at least 1")
    
    angles = np.linspace(start_angle, start_angle + 2*np.pi, n, endpoint=False)
    x_coords = center[0] + radius * np.cos(angles)
    y_coords = center[1] + radius * np.sin(angles)
    
    return x_coords.tolist(), y_coords.tolist()

def plot_circle_points(n, radius=1, center=(0, 0), start_angle=0, 
                      show_circle=True, show_connections=False, 
                      point_size=50, figsize=(8, 8)):
    """Plot n equally spaced points on a circle perimeter."""
    # Generate points
    x_coords, y_coords = generate_circle_points(n, radius, center, start_angle)
    
    # Create the plot
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the circle outline if requested
    if show_circle:
        circle_angles = np.linspace(0, 2*np.pi, 100)
        circle_x = center[0] + radius * np.cos(circle_angles)
        circle_y = center[1] + radius * np.sin(circle_angles)
        ax.plot(circle_x, circle_y, 'b--', alpha=0.5, linewidth=1, label='Circle')
    
    # Plot the points
    ax.scatter(x_coords, y_coords, s=point_size, c='red', zorder=5, label='Particles')
    
    # Connect points if requested
    if show_connections:
        x_polygon = np.append(x_coords, x_coords[0])
        y_polygon = np.append(y_coords, y_coords[0])
        ax.plot(x_polygon, y_polygon, 'g-', linewidth=2, alpha=0.7, label='Connections')
    
    # Annotate points with their index
    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
        ax.annotate(f'P{i}', (x, y), xytext=(5, 5), textcoords='offset points',
                   fontsize=10, ha='left')
    
    # Mark center
    ax.plot(center[0], center[1], 'ko', markersize=8, label='Center')
    
    # Set equal aspect ratio and formatting
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'{n} Charged Particles - Equilibrium Configuration')
    
    # Add padding around the circle
    padding = radius * 0.2
    ax.set_xlim(center[0] - radius - padding, center[0] + radius + padding)
    ax.set_ylim(center[1] - radius - padding, center[1] + radius + padding)
    
    plt.tight_layout()
    return fig

def coefficientgen(num):
    """Generate distance coefficients for particles on circle."""
    arr1, arr2 = generate_circle_points(num)
    arr = np.column_stack((arr1, arr2))
    dx = (arr[0][0] - arr[1][0])
    dy = (arr[0][1] - arr[1][1]) 
    l = np.sqrt(dx**2 + dy**2)
    dmat = compute_distance_matrix(arr)
    return np.array(dmat), l

def find_roots(func, a=0, b=10, steps=1000, atol=1e-10, variable=None):
    """Find roots of a function using numerical methods."""
    if hasattr(func, 'free_symbols'):
        if variable is None:
            free_symbols = func.free_symbols
            if len(free_symbols) == 1:
                variable = list(free_symbols)[0]
            else:
                raise ValueError("Multiple variables found")
        numerical_func = sp.lambdify(variable, func, 'numpy')
    else:
        numerical_func = func
    
    x = np.linspace(a, b, steps)
    roots = []
    
    for i in range(len(x) - 1):
        x0, x1 = x[i], x[i + 1]
        try:
            y0, y1 = numerical_func(x0), numerical_func(x1)
            if np.sign(y0) != np.sign(y1):
                try:
                    root = brentq(numerical_func, x0, x1)
                    if not any(np.isclose(root, r, atol=atol) for r in roots):
                        roots.append(root)
                except ValueError:
                    pass
        except (ValueError, ZeroDivisionError, OverflowError):
            continue
    
    return sorted(roots)

def calculate_equilibrium(nums, lam_da, z, k):
    """Calculate equilibrium spacing for given parameters."""
    try:
        # Set up potential object
        p = potential(lam_da, z, k)
        l = symbols("l")
        
        # Get distance coefficients
        lengths, c = coefficientgen(nums)
        r = l/c
        lengths = lengths/c
        
        # Construct energy equation
        exp = nums * p.confinement(r)
        for i in lengths:
            exp += p.interaction(i*l)
        
        # Take derivative
        dff = diff(exp, l)
        diff2 = diff(dff, l)
        
        # Find roots
        roots = find_roots(dff, 0.0001, 3e-3, 10000)
        
        # Filter out maxima and inflection points
        valid_roots = []
        for root in roots:
            try:
                second_deriv = float(diff2.subs(l, root).evalf())
                if second_deriv > 0:  # Minimum condition
                    valid_roots.append(root)
            except:
                continue
        
        return valid_roots, exp, dff
    
    except Exception as e:
        st.error(f"Calculation error: {str(e)}")
        return [], None, None

# Streamlit App
def main():
    st.title("⚛️ Charged Particles Equilibrium Simulation")
    st.markdown("Find the optimal spacing of charged particles arranged on a circle")
    
    # Sidebar for parameters
    st.sidebar.header("Parameters")
    
    # Number of particles
    nums = st.sidebar.slider("Number of Particles", min_value=2, max_value=10, value=3)
    
    # Physical parameters
    st.sidebar.subheader("Physical Constants")
    lam_da = st.sidebar.number_input("Lambda (λ) - Screening Length", 
                                    value=300e-6, format="%.2e",
                                    help="Screening length parameter")
    
    z = st.sidebar.number_input("Charge (z)", 
                               value=-7000.0,
                               help="Particle charge")
    
    k = st.sidebar.number_input("Confinement Strength (k)", 
                               value=-1000.0,
                               help="Confinement potential strength")
    
    # Calculation button
    if st.sidebar.button("Calculate Equilibrium", type="primary"):
        with st.spinner("Calculating equilibrium configuration..."):
            roots, energy_expr, derivative_expr = calculate_equilibrium(nums, lam_da, z, k)
            
            if roots:
                st.success(f"Found {len(roots)} equilibrium configuration(s)!")
                
                # Display results
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📊 Results")
                    for i, root in enumerate(roots):
                        st.metric(f"Equilibrium Distance {i+1}", f"{root:.6f}")
                
                with col2:
                    st.subheader("🔬 Parameters Used")
                    st.write(f"**Particles:** {nums}")
                    st.write(f"**λ:** {lam_da:.2e}")
                    st.write(f"**z:** {z:.0f}")
                    st.write(f"**k:** {k:.0f}")
                
                # Plot the particle arrangement
                st.subheader("🎯 Particle Arrangement")
                
                # Use the first (most stable) root for visualization
                optimal_l = roots[0]
                
                # Plot options
                col1, col2, col3 = st.columns(3)
                with col1:
                    show_circle = st.checkbox("Show Circle", value=True)
                with col2:
                    show_connections = st.checkbox("Show Connections", value=False)
                with col3:
                    point_size = st.slider("Point Size", 20, 200, 80)
                
                # Create and display the plot
                fig = plot_circle_points(nums, radius=1, show_circle=show_circle, 
                                       show_connections=show_connections, 
                                       point_size=point_size, figsize=(8, 8))
                st.pyplot(fig)
                
                # Additional information
                st.subheader("📈 Energy Analysis")
                st.write(f"**Optimal nearest-neighbor distance:** {optimal_l:.6f}")
                st.write(f"**Number of minima found:** {len(roots)}")
                
                if len(roots) > 1:
                    st.write("**All equilibrium distances:**")
                    for i, root in enumerate(roots):
                        st.write(f"  - Configuration {i+1}: {root:.6f}")
                
                # Show energy equation (optional)
                with st.expander("Show Energy Equation"):
                    if energy_expr:
                        st.latex(r"\text{Energy} = " + str(energy_expr))
            else:
                st.error("No equilibrium configuration found. Try adjusting the parameters.")
                st.info("Suggestions:\n- Increase the number of particles\n- Adjust λ, z, or k values\n- Check that parameters are physically reasonable")
    
    # Information section
    st.markdown("---")
    st.subheader("ℹ️ About This Simulation")
    st.markdown("""
    This simulation models charged particles constrained to move on a circle, subject to:
    
    1. **Screened Coulomb Interactions**: Particles repel/attract with exponentially screened potential
    2. **Confinement Potential**: Quadratic potential keeping particles near the circle
    
    The simulation finds the nearest-neighbor distance that minimizes the total energy of the system.
    
    **Parameters:**
    - **λ (Lambda)**: Screening length - controls how quickly interactions decay
    - **z**: Particle charge - determines interaction strength  
    - **k**: Confinement strength - controls how tightly particles are bound to circle
    """)

if __name__ == "__main__":
    main()