import numpy as np

A = np.array([
    [0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0]
], dtype = "f")

def transition_matrix(matrix):
    A = matrix.copy()
    for i in  range(A.shape[0]):
        if A[i,].sum() != 0:
            A[i,] *= 1/A[i,].sum()
    return A

def stochastic_matrix(matrix):
    A = matrix.copy()
    for i in  range(A.shape[0]):
        if A[i,].sum() != 0:
            A[i,] *= 1/A[i,].sum()
        else:
            A[i,] += 1/A.shape[0]
    return A

def google_matrix(matrix, alpha):
    A = matrix.copy()
    google_matrix = alpha*A + (1-alpha)*np.full((A.shape[0], A.shape[0]), 1/A.shape[0])
    return google_matrix

A = np.matrix(google_matrix(stochastic_matrix(A), 0.9))
p = np.matrix(np.full((1, A.shape[0]), 1/A.shape[0]))

for i in range(50):
    p = p*A
    print(p)
    
