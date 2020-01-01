from matplotlib import pyplot as plt
import random

x = range(1, 32)
y1 = [random.randint(10, 30) for i in range(31)]
y2 = [random.randint(10, 30) for i in range(31)]

barwidth=0.3
# 绘制柱状图
plt.figure(figsize = (15,3))
plt.bar([i for i in x], y1, width=barwidth)  # 纵向  宽
plt.bar([i+barwidth for i in x], y2,width=barwidth )  # barh 横向  高 height=0.8
plt.xticks(x)
plt.savefig("t3.png")
