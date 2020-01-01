from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

#创建字体
my_font = font_manager.FontProperties(fname="Arial Unicode.ttf")
#设定图片的大小与清晰度
fig = plt.figure(figsize = (10,3),dpi=80)
#给定数据
x = range (2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]
z = [25,23,24.5,27,30,35,36,36,34,33,28,25]
#指定X、y刻度 可传两个对应列表或者元组，如果传输一个，默认用X做刻度，不会替换为文本
plt.xticks(range(2,26,4),["-甲","-乙","-丙","-丁","-庚","-辛"],rotation=45,fontproperties=my_font) # rotation 旋转角度 fontproperties 指定字体
plt.yticks(range(min(y),max(y)+1))
#添加描述信息
plt.xlabel("X轴说明",fontproperties=my_font)
plt.ylabel("Y轴说明",fontproperties=my_font)
plt.title("图标的标题",fontproperties=my_font)
#绘制网格
plt.grid(alpha = 0.2) # alpha 透明度

#绘图
plt.plot(x,y,label="第一条线的图例",color="blue",linestyle = ":",linewidth = 5) #label 添加图例
plt.plot(x,z,label="第二条线的图例",color="green",linestyle = "--",linewidth = 2) #可以绘制多个线条
plt.legend(loc=0,prop=my_font) # 只有这个地方是 prop 其他地方是 fontproperties loc位置
#保存
plt.savefig("t.png")
# plt.show()

# 还可以添加最高最低值  水印等