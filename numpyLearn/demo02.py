import numpy as np
t1=np.arange(12).reshape(3,4)
print(t1)
print(t1[2,3])
print(t1[:-1,-1:])
print(t1[:,(1,3)])
print(t1[(0,2),(1,3)])