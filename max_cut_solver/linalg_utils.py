from scipy.linalg import sqrtm
import numpy as np


def get_square_root_of_matrix(matrix):
    return sqrtm(matrix)


def random_vector(num_dims):
    return np.random.randn(num_dims)
