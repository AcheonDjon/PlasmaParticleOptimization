import numpy as np

def compute_distance_matrix(points):
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    distance_matrix = np.linalg.norm(diff, axis=2)
    
    # Get upper triangular part (excluding diagonal)
    indices = np.triu_indices(len(points), k=1)
    distances = distance_matrix[indices]
    
    return distances
