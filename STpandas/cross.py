import pandas as pd
import numpy as np
# Series 带标签的一维数组
# t1 = pd.Series([1,2,3,4,5,7],index=["a","b","c","e","e","f"]) # index 索引 默认从0开始
# data = {"name":"cc","age":27,"sex":1}
# t2 = pd.Series(data) #输出类型
# t1 = t1.astype("float")  #改变类型
# print(t2["age"])#通过索引取值 强制去没有的值 返回Nan
# print(t2[2])#通过位置取值
# print(t2[["name","age"]])#通过位置取值
# print(t2[0:2])#通过位置取值
# print(t1[t1>4])# 布尔索引取值
# print(t2.index,t2.values)#输出键、值

t1 = pd.DataFrame(np.arange(1,91).reshape(9,10),index=["a","b","c","d","e","f","g","h","i"],columns=range(1,11))
data = {"name":["cc","haha"],"age":[27,28],"sex":[1,1]}
t2 = pd.DataFrame(data)
print(t2[0:])
# data = [{"name":"cc","age":27,"sex":1},{"name":"hh","age":28}] # 可以缺失值  缺失为NAN
# t3 = pd.DataFrame(data)
# print(t3)
# print(t3.index) # index 列表
# print(t3.columns) # cloumns 列表
# print(t3.values) # 值
# print(t3.shape) # 形状
# print(t3.ndim) #数据维度
# print(t3.dtypes) # 数据类型
# print(t3.head(2)) # 默认5
# print(t3.tail(2)) # 默认3
# print(t3.info()) # 信息
# print(t3.describe()) #统计数值类型的列的统计学信息

# print(t3)
# t4 = t3.sort_values(by="age",ascending=False) # ascending=False 降序
# print(t4)
# print(t3[:1])# 切片
# print(t3[:1]["sex"])# 切片
# print(t1.loc["a",2]) # loc 通过标签获取 取a行2列
# print(t1.loc[["a","e"],[2]]) # 取a行2列
# print(t1.loc[2,2]) # loc 通过标签获取 取a行2列
# print(t1.iloc[[2,3],[2]]) #iloc 通过位置获取 取a行2列
# print(t1.iloc[[2,3,5],[2,6,8]]) #iloc 通过位置获取 取a行2列
# t1.iloc[[2,3,5],[2,6,8]] = 30
# print(t1)