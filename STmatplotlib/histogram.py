from matplotlib import pyplot as plt
import random

x = range(100)
a = [random.randint(100, 199) for i in range(100)]

print(min(a),max(a))
gap=5
num_bins=(max(a)-min(a)) //gap+1
print(num_bins)
# 绘制直方图
plt.hist(a,num_bins,range=(min(a),min(a)+num_bins*gap)) # density=True 修改为频率直方图 range 起止范围
plt.xticks(range(min(a),max(a)+gap,gap),rotation=45)# min max 组距
plt.grid(alpha = 0.5) # alpha 透明度
plt.savefig("t4.png")
