import numpy as np


array = np.random.randint(10, size=(3, 3))

inverse_matrix = np.linalg.inv(array)
rank = np.linalg.matrix_rank(array)
det = np.linalg.det(array)
flat_array = array.flatten()
w,v = np.linalg.eig(array)

print(flat_array)
print("Inverse of matrix:\n",inverse_matrix)
print("Squre Matrix:\n",array)
print('1D Numpy Array:\n',flat_array)
print("Eigon value:\n",w)
print("Eigon vector:\n",v)