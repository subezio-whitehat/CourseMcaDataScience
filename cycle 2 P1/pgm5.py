import numpy as np
a = np.arange(0,15,2)
print(a)
print("Elements from index 2 to 8 ")
print(a[2:8:2])
print("last 3 elements using -ve index :",a[-3:])
print("Alternate elements:",a[-5::2])
