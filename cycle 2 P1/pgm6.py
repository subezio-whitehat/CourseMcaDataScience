import numpy as np
x =np.arange(1,33,2).reshape(4,4)
print(x)
print("Excluding first row :",x[1:])
print("Excluding last column :",x[:, :3])
print("Elements of 2nd and 3rd column:",x[:,1:3])
print("Elements of 1st and 2nd column in 2nd and 3rd row:",x[1:3,:2])
print("2nd and 3rd elements of 1st row:",x[:1,1:3])