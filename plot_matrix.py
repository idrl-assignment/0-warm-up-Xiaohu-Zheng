# TODO: import ...

import numpy as np
from scipy import misc


def generate_random_matrix(m, n):
    mat01 = np.random.randint(0, 2, (m, n))
    return mat01


def save_matrix(matrix, file_name):
    misc.imsave('example.jpg', matrix)


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
