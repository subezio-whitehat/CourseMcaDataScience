import numpy as np
array = np.array([[1,3,5], [3, 4,6]],dtype ="complex")
print(array)
print("no of rows and column",array.shape)
narr = array.reshape(3,2)
print("reshape\n",narr)
print("dimension\n",array.ndim)
      