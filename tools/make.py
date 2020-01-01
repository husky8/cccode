from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import datetime
from tools import logic
from tools import getSomething







def makePicture(name=None,string=None,fontSize='Auto',fontColor=None,picSize=None,bg=None):
    # 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
    if not logic.isColor(bg):
        print("未指定颜色或者颜色输入不正确，将使用随机颜色")
        bg = getSomething.getRandomColor()

    if not logic.isRect(picSize):
        print("未指定画布大小或者画布大小输入不正确，将使用默认尺寸（400，300）")
        picSize=(400,300)

    if not name:
        name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')+'.png'
    image = Image.new('RGB', picSize, bg)

    if fontSize == 'auto':
        if not string:
            fontSize=26
        else:
            fontSize=min(int(picSize[0]/1.2/max([len(i) for i in string.split("\n")])),int(picSize[1]/1.2/len(string.split("\n"))))
    print(fontSize)
    print(min(int(picSize[0]/1.2/max([len(i) for i in string.split("\n")]))
                         ,int(picSize[1]/1.2/len(string.split("\n")))))
    print(int(picSize[1]/1.2/len(string.split("\n"))))

    # 获取一个画笔对象，将图片对象传过去
    draw = ImageDraw.Draw(image)

    # 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
    font = ImageFont.truetype("Arial Unicode.ttf", size=fontSize)



    if not string:
        for i in range(5):
            # 循环5次，获取5个随机字符串
            random_char = getSomething.getRandomStr()

            # 在图片上一次写入得到的随机字符串,参数是：定位，字符串，颜色，字体
            draw.text((10 + i * 30, 0), getSomething.random_char, getSomething.getRandomColor() if not fontColor else fontColor , font=font)
    else:
        for i in range(len(string.split("\n"))):
            str_cut = string.split("\n")[i]
            for j in range(len(str_cut)):
                random_char = str_cut[j]
                draw.text((10 + fontSize * j * 1.2, fontSize * i *1.2), random_char , getSomething.getRandomColor() if not fontColor else fontColor, font=font)


    # 保存到硬盘，名为test.png格式为png的图片
    image.show()
    image.save(name)
# print(isColor((255,255,255)))
makePicture(picSize=(800,533),fontSize='auto',fontColor=(0,0,255),string='首页百科\n每日一品\n № 95'
            ,name='/Users/smzdm/Documents/pic/每日一品.png')