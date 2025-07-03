import numpy as np

def compute_distance_matrix(points):
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    distance_matrix = np.linalg.norm(diff, axis=2)
    
    # Get upper triangular part (excluding diagonal)
    indices = np.triu_indices(len(points), k=1)
    distances = distance_matrix[indices]
    
    return distances
# def compute_distance_matrix(points):
#     diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
#     distance_matrix = np.linalg.norm(diff, axis=2)
#     distance_matrix = distance_matrix.flatten().tolist()
#     half  = len(distance_matrix)//2
#     if len(distance_matrix)%2 == 0:
#         distance_matrix = distance_matrix[:half]
#     else:
#         distance_matrix = distance_matrix[:half+1]
#     cleaned = [x for x in distance_matrix if x != 0]
#     return cleaned

# Example usage
# points = [(1, 2), (4, 6), (0, 0), (3, 3),(9,9)]
# dist_matrix = compute_distance_matrix(points)

# print("Distance Matrix:")
# print(len(dist_matrix))
