import pandas as pd
from pandas import DataFrame


# data = pd.read_excel("配置.xlsx","zz500")
# print(data)
# DataFrame(data).to_excel('example.xlsx', sheet_name='Sheet1', index=False, header=True)

import numpy as np
my_array = np.array([1, 2, 3, 4, 5])

print(my_array.shape)
# [out] (5,) 获取数组的形状

print(my_array[0])
# [out] 1 获取数组的指定元素

my_array[0] = -1
print (my_array)
# [out] [-1  2  3  4  5] 修改数组的元素

my_new_array = np.zeros((5))
print my_new_array

my_new_array = np.zeros((5))
print my_new_array