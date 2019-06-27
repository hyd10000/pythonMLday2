import numpy as np

t1=np.arange(12)

print(t1,type(t1),t1.shape)

t1=t1.reshape(3,4)
print(t1,type(t1),t1.shape)

print('矩阵的形状',t1.shape,'矩阵元素数量',t1.size)
print('矩阵内元素的数据类型',t1.dtype,'矩阵内元素的占用空间',t1.itemsize)

t1=t1.astype(np.float64)
print('矩阵内元素的数据类型',t1.dtype,'矩阵内元素的占用空间',t1.itemsize)

#nparray与list的区别
#矩阵运算
print(t1+1)
#矩阵不能直接算
#l=[1,2,3,4,5]
#print(l+1)

#创建矩阵的第二种方式
data=[[1,2,3],[4,5,6],[7,8,9]]
t1=np.array(data)
print(t1,type(t1),t1.shape)

#创建矩阵的第三种方式
#生成随机数矩阵
l= np.random.randint(4,100,size=[3,4])
print(l)