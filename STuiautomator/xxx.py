
from PIL import Image


from PIL import Image


def saveblack(img):
    img = img.convert("RGBA")  # 转换获取信息
    pixdata = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            # print(pixdata[x, y])
            if pixdata[x, y][2] > 185 or abs(pixdata[x, y][2]-pixdata[x, y][1]) <3 :
                pixdata[x, y] = (255, 255, 255, 1)
    return img



image = Image.open('xx.gif')
img_s = image.crop((121, 969, 521, 1111))
img_s = saveblack(img_s)
img_s.show()
