import numpy as np
t1 = np.loadtxt("hs300history.csv",skiprows=1,delimiter=',',dtype="int")
t2 = np.loadtxt("hs300history.csv",skiprows=1,delimiter=',',dtype="int")
# frame 文件、字符串、常生气 .gz .bz2文件
# dtype 数据类型 默认np.float
# delimiter 默认分割符
# skiprows 跳过前X行
# usecols 读取指定的列
# unpack 如果是True 转置 行列互换
# print(t1)
# print("*"*100)
# print(t1[1,4]) # 取1行4列  支持 t1[:,4] ti[4]
# print(t1[:,4])
# print(t1[:,[4,]]) # 传list 避免接收到一个数组内
# print(t1[[0,1],[2,3]]) # 取出 0，2   1，3 两个数值
# t1[[0,1],[2,3]] = 888 #
# print("*"*100)#赋值
# print(t1)
# print(t1<1000)
# t1[t1<1000] = 11111 # 布尔替换
# print(t1)
# t1 = np.where(t1<10000,11111,2222) # 三元运算符
# print(t1)
# t1 = t1.clip(222,3333) # 裁剪 小于222替换成222 大于3333替换成3333
# print(t1)
# t3 = np.vstack((t1,t2)) # 竖直拼接
# t4 = np.hstack((t1,t2)) # 水平拼接
# print(t3)
# print(t4)
# print(np.vsplit(t1,[0,2])) # 竖直分割
# print(np.hsplit(t1,[0,2])) # 水平分割
t = np.arange(24)
t=t.reshape((4,6))
print(t)
t[[1,2],:] = t[[2,1],:] #行交换
print(t)

