import  numpy as np
import random

# 读数据
# data = np.loadtxt(frame,dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False)
# frame 文件、字符串、常生气 .gz .bz2文件
# dtype 数据类型 默认np.float
# delimiter 默认分割符
# skiprows 跳过前X行
# usecols 读取指定的列
# unpack 如果是True 转置 行列互换

# data = np.loadtxt("hs300history.csv",skiprows=1,delimiter=",",dtype="int")
# print(data[0])
# t1 = np.array([1,2,3])
# t2 = np.array(range(10),dtype="int32") #dtype 指定数据类型
# t3 = np.arange(10)
#
# # 调整数据类型
# t4 = t3.astype("int8")
#
# print(type(t1),type(t2),type(t3),type(t4))
# print(t1.dtype,t2.dtype,t3.dtype,t4.dtype)
# t5 = np.array([random.random() for i in range(10)])
# t5 = np.round(t5,2) # 取小数
# print(t5)


