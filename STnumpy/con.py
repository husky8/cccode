import numpy as np

t1 = np.arange(24)
t1 = t1.reshape((4,6))

t2 = np.arange(24,48)
t2 = t2.reshape((4,6))
t3 = np.eye(10)
# print(np.argmax(t3,1)) # 获取1 = 列最大值位置
# print(np.argmin(t3,0)) # 获取0 = 行最小值位置

# print(t1,t2)
# zerodata = np.zeros((t1.shape[0],1)).astype("int")
# onesdata = np.ones((t2.shape[0],1)).astype("int")
# t1 = np.hstack((t1,zerodata))
# t2 = np.hstack((t2,onesdata))
# print(t1,t2)
# findata = np.vstack((t1,t2))
# print(findata)
# t3 = np.eye(5) #创建对角线为1 长宽为的i数组
# print(t3)
# t4 = np.random.rand(2,3) # 标准分布随机图形
# print(t4)
# t4 = np.random.randn(2,3) # 正态分布随机图形
# print(t4)
# np.random.seed(10086) # 指定随机种子 后续生效
# t4 = np.random.randint(0,10,(6,6)) # 随机起（含)止(不含）范围整数
# print(t4)
#ta = tb  ta = tb[:] 浅拷贝 a= b.copy() 深拷贝
# nan inf 都是浮点型 np.nan != np.nan  nan和任何值计算结果都是nan
# t2=t2.astype(float)
# t2[:,5] = 0
# t2[3,4] = np.nan
# print(np.sum(t2))
# print(np.sum(t2,axis=0)) #计算0轴（列）的求和结果
# print(np.sum(t2,axis=1)) #计算1轴（行）的求和结果
# print(np.mean(t2,axis=0)) #均值
# print(np.median(t2,axis=0)) #中值 有nan报错
# print(np.ptp(t2,axis=0)) #极值
# print(np.std(t2,axis=0)) #标准差
# print(t2)
# print(np.count_nonzero(t2)) # 输出t2不为0的元素的个数
# print(np.isnan(t2))

t1 = np.arange(30).reshape((5,6)).astype("float")
t1[1,2:] = np.nan
print(t1)
for i in range(t1.shape[1]):
    col = t1[:,i]
    # colavg = np.mean(col)
    # print(colavg)j
    if np.isnan(np.mean(col)):
        colmean = np.nanmean(col)
        for j in range(t1.shape[0] ):
            if np.isnan(t1[j,i]):
                t1[j,i] = colmean
print(t1)
