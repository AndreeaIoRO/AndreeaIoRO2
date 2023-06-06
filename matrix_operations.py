import numpy as np

def matrix_multiply(a, b):
    return np.dot(a, b)

def matrix_transpose(a):
    return np.transpose(a)

def matrix_inverse(a):
    return np.linalg.inv(a)

def matrix_determinant(a):
    return np.linalg.det(a)

def matrix_eigenvalues(a):
    return np.linalg.eigvals(a)

def matrix_rank(a):
    return np.linalg.matrix_rank(a)

def matrix_trace(a):
    return np.trace(a)

def matrix_power(a, n):
    return np.linalg.matrix_power(a, n)

if __name__ == '__main__':
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])

    result_multiply = matrix_multiply(matrix_a, matrix_b)
    print("Matrix Multiplication:")
    print(result_multiply)

    result_transpose = matrix_transpose(matrix_a)
    print("\nMatrix Transpose:")
    print(result_transpose)

    result_inverse = matrix_inverse(matrix_a)
    print("\nMatrix Inverse:")
    print(result_inverse)

    result_determinant = matrix_determinant(matrix_a)
    print("\nMatrix Determinant:")
    print(result_determinant)

    result_eigenvalues = matrix_eigenvalues(matrix_a)
    print("\nMatrix Eigenvalues:")
    print(result_eigenvalues)

    result_rank = matrix_rank(matrix_a)
    print("\nMatrix Rank:")
    print(result_rank)

    result_trace = matrix_trace(matrix_a)
    print("\nMatrix Trace:")
    print(result_trace)

    result_power = matrix_power(matrix_a, 3)
    print("\nMatrix Power:")
    print(result_power)
