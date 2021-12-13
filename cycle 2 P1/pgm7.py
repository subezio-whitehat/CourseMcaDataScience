import numpy as np
x1=np.arange(1,5,1).reshape((2,2))
x2=np.arange(1,5,1).reshape((2,2))
#1
a=np.add(x1,x2)
print("The addition result",a)
#2
a=np.subtract(x1,x2)
print("The substract value is",a)
#3
a=np.multiply(x1,x2)
print("The mulitiplication of individual elements",a)
#4.
a=np.divide(x1,x2)
print("The division of individual element",a)
#5.
a=np.matmul(x1,x2)
print("The result is",a)
#6.
a=x1.transpose()
print("The transpose is",a)
#7.
a=np.trace(x1)
print("The sum of diagonal elements",a)


