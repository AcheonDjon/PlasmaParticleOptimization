import numpy as np

def compute_distance_matrix(points):
    """
    Compute the pairwise Euclidean distance matrix for a list of 2D or nD points.
    
    Parameters:
        points (list of tuples or 2D np.array): e.g., [(x1, y1), (x2, y2), ...]
    
    Returns:
        np.array: A square distance matrix (N x N)
    """
    points = np.array(points)
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    distance_matrix = np.linalg.norm(diff, axis=2)
    distance_matrix = distance_matrix.flatten().tolist()
    half  = len(distance_matrix)//2
    if len(distance_matrix)%2 == 0:
        distance_matrix = distance_matrix[:half]
    else:
        distance_matrix = distance_matrix[:half+1]
    cleaned = [x for x in distance_matrix if x != 0]
    return cleaned

# Example usage
# points = [(1, 2), (4, 6), (0, 0), (3, 3),(9,9)]
# dist_matrix = compute_distance_matrix(points)

# print("Distance Matrix:")
# print(len(dist_matrix))
