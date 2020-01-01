from matplotlib import pyplot as plt
from matplotlib import font_manager

import random
x = range(1,32)
y1 = [ random.randint(10,30) for i in range(31)]
y2 = [ random.randint(10,30) for i in range(31)]


# 绘制散点图
plt.scatter(x,y1)
plt.scatter(x,y2)
plt.savefig("t2.png")