import numpy as np
A = np.array([[2, 1,-2], [3, 0,1],[1,1,-1]])
b = np.array([[-3],[5],[-2]])
inverse_matrix = np.linalg.inv(A)

sol = np.linalg.solve(inverse_matrix,b)
print("Matrix A:",A)
print("Matrix b:",b)
