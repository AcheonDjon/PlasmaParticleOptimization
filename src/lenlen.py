import numpy as np
import matplotlib.pyplot as plt
from distancemat import compute_distance_matrix

def generate_circle_points(n, radius=1):
    # Calculate angles for equally spaced points on the circle
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    
    # Calculate coordinates
    x_coords = radius * np.cos(angles)
    y_coords = radius * np.sin(angles)
    
    return x_coords.tolist(), y_coords.tolist()
def coefficientgen(num):
    arr1,arr2 = generate_circle_points(num)
    arr = np.column_stack((arr1,arr2))
    print(arr)
    dx = (arr[0][0] - arr[1][0])
    dy = (arr[0][1]- arr[1][1]) 
    l = np.sqrt(dx**2 + dy**2)
    dmat = compute_distance_matrix(arr)
    return dmat, l

# def plot_circle_points(n, radius=1, center=(0, 0), start_angle=0, 
#                       show_circle=True, show_connections=False, 
#                       point_size=50, figsize=(8, 8)):
#     """
#     Plot n equally spaced points on a circle perimeter.
    
#     Parameters:
#         n (int): Number of points
#         radius (float): Circle radius
#         center (tuple): Circle center (x, y)
#         start_angle (float): Starting angle in radians
#         show_circle (bool): Whether to draw the circle outline
#         show_connections (bool): Whether to connect points with lines
#         point_size (int): Size of the plotted points
#         figsize (tuple): Figure size
#     """
#     # Generate points
#     x_coords, y_coords = generate_circle_points(n, radius, center, start_angle)
    
#     # Create the plot
#     fig, ax = plt.subplots(figsize=figsize)
    
#     # Plot the circle outline if requested
#     if show_circle:
#         circle_angles = np.linspace(0, 2*np.pi, 100)
#         circle_x = center[0] + radius * np.cos(circle_angles)
#         circle_y = center[1] + radius * np.sin(circle_angles)
#         ax.plot(circle_x, circle_y, 'b--', alpha=0.5, linewidth=1, label='Circle')
    
#     # Plot the points
#     ax.scatter(x_coords, y_coords, s=point_size, c='red', zorder=5, label='Points')
    
#     # Connect points if requested (creates polygon)
#     if show_connections:
#         # Close the polygon by adding the first point at the end
#         x_polygon = np.append(x_coords, x_coords[0])
#         y_polygon = np.append(y_coords, y_coords[0])
#         ax.plot(x_polygon, y_polygon, 'g-', linewidth=2, alpha=0.7, label='Connections')
    
#     # Annotate points with their index
#     for i, (x, y) in enumerate(zip(x_coords, y_coords)):
#         ax.annotate(f'P{i}', (x, y), xytext=(5, 5), textcoords='offset points',
#                    fontsize=10, ha='left')
    
#     # Mark center
#     ax.plot(center[0], center[1], 'ko', markersize=8, label='Center')
    
#     # Set equal aspect ratio and formatting
#     ax.set_aspect('equal')
#     ax.grid(True, alpha=0.3)
#     ax.legend()
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_title(f'{n} Equally Spaced Points on Circle (Radius = {radius})')
    
#     # Add some padding around the circle
#     padding = radius * 0.2
#     ax.set_xlim(center[0] - radius - padding, center[0] + radius + padding)
#     ax.set_ylim(center[1] - radius - padding, center[1] + radius + padding)
    
#     plt.tight_layout()
#     plt.show()
    
#     return x_coords, y_coords

