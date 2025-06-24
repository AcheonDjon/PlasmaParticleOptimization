import matplotlib.pyplot as plt
import numpy as np

def visualize_particles(nums, l):
    """
    Visualize the arrangement of particles along a line.
    Args:
        nums (int): Number of particles
        l (float): Total length (distance between outermost particles)
    """
    if nums < 2:
        raise ValueError("At least 2 particles are required.")
    positions = np.linspace(-l/2, l/2, nums)
    y = np.zeros(nums)
    plt.figure(figsize=(6, 2))
    plt.scatter(positions, y, s=200, c='red')
    for i, x in enumerate(positions):
        plt.text(x, 0.05, f'Particle {i+1}', ha='center')
    plt.title(f'Arrangement of {nums} Particles')
    plt.xlabel('x')
    plt.yticks([])
    plt.grid(True, axis='x')
    plt.show()
