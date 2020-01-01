import numpy as np
t1 = np.arange(12)
print(t1.shape)
t2 = np.array([[1,2,3],[4,5,6]])
print(t2.shape)
t3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
               [[13,14,15,16],[17,18,19,20],[21,22,23,24]]
               ])
print(t3.shape)
t4 = np.arange(60)
print(t4.shape)
t4 = t4.reshape((3,4,5)) # 形状转换 由外到内的层数
print(t4)
t4 = t4.reshape(4,15)
print(t4)
# t4 = t4.flatten()
# print(t4.shape) # 展开形状
t5 = t4+2 # 利用广播机制 每个元素单独加2
t6 = np.arange(15)
t7 = np.arange(4).reshape(4,1)
print(t7)
# print(t4 / 0)
print(t4+t5) # 利用广播机制 每个对应元素单独计算
print(t4+t6) # 如果某一维度形状相同，以相同位置进行计算
print(t4+t7)

# 转置
print(t7)
print(t7.transpose())
print(t7.T)
print(t7.swapaxes(1,0)) # 交换 0轴 和 1 轴
