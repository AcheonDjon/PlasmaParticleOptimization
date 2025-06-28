import matplotlib.pyplot as plt
import numpy as np

def visualize_particles(nums, l, ax=None):
    """
    Visualize the arrangement of particles along a line.
    Args:
        nums (int): Number of particles
        l (float): Total length (distance between outermost particles)
        ax (matplotlib.axes.Axes, optional): Axes to plot on. If None, creates a new figure.
    """
    if nums < 2:
        raise ValueError("At least 2 particles are required.")
    positions = np.linspace(-l/2, l/2, nums)
    y = np.zeros(nums)
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 2))
    ax.scatter(positions, y, s=200, c='red')
    for i, x in enumerate(positions):
        ax.text(x, 0.05, f'Particle {i+1}', ha='center')
    ax.set_title(f'Arrangement of {nums} Particles')
    ax.set_xlabel('x')
    ax.set_yticks([])
    ax.grid(True, axis='x')
    # Do not call plt.show() here
