import uiautomator2 as u2
import pytesseract
import time
from PIL import ImageChops
from PIL import Image
import random


def saveblack(img):
    img = img.convert("RGBA")  # 转换获取信息
    pixdata = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):

            if pixdata[x, y][0] > 120 or pixdata[x, y][1] > 120 or pixdata[x, y][2] > 120:
                pixdata[x, y] = (255, 255, 255, 1)
    return img

def saveblackorredorgreen(img):
    img = img.convert("RGBA")  # 转换获取信息
    pixdata = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            # print(pixdata[x, y])
            if  pixdata[x, y][2] > 185 or abs(pixdata[x, y][2]-pixdata[x, y][1]) <3 :
                pixdata[x, y] = (255, 255, 255, 1)
    return img


res = open("res2.txt", "w", encoding="utf-8")
d = u2.connect()
lastcoded = 0
xpos = 907/1080
while xpos < 0.93:
    print(xpos)
    # xpos = round(xpos + (1000-440)/1080/50, 4)
    xpos = round(xpos + 0.001, 4)

    d.click(xpos, random.randint(666, 777) / 1000)
    d.screenshot("xx.gif")
    image = Image.open('xx.gif')
    # 日
    # img_d = image.crop((222, 1250, 1080, 1305))
    # 总
    img_d = image.crop((265, 1240, 1015, 1305))

    img_d = ImageChops.invert(img_d)
    img_d = saveblack(img_d)
    coded = pytesseract.image_to_string(img_d)
    print(coded)
    if coded == lastcoded:
        continue

    # 日收益解析
    # img_t = image.crop((280, 689, 843, 825))
    # img_t = saveblackorredorgreen(img_t)
    # img_yeb = image.crop((121, 861, 521, 966))
    # img_yeb = saveblackorredorgreen(img_yeb)
    # img_lc = image.crop((521, 861, 955, 969))
    # img_lc = saveblackorredorgreen(img_lc)
    # img_jj = image.crop((121, 969, 521, 1111))
    # img_jj = saveblackorredorgreen(img_jj)
    # img_hj = image.crop((555, 980, 999, 1111))
    # img_hj = saveblackorredorgreen(img_hj)

    # 总收益解析
    img_t = image.crop((280, 689, 843, 825))
    img_t = saveblackorredorgreen(img_t)
    img_yeb = image.crop((121, 861, 521, 966))
    img_yeb = saveblackorredorgreen(img_yeb)
    img_lc = image.crop((521, 861, 955, 969))
    img_lc = saveblackorredorgreen(img_lc)
    img_jj = image.crop((121, 969, 521, 1111))
    img_jj = saveblackorredorgreen(img_jj)
    img_hj = image.crop((555, 980, 999, 1111))
    img_hj = saveblackorredorgreen(img_hj)


    img_t.save("xxt.gif")
    img_yeb.save("xxyeb.gif")
    img_lc.save("xxlc.gif")
    img_jj.save("xxjj.gif")
    img_hj.save("xhj.gif")
    # img_s.save("xxs.jpg")
    # img_d.save("xxd.jpg")

    codet = pytesseract.image_to_string(img_t)
    codeyeb = pytesseract.image_to_string(img_yeb)
    codelc = pytesseract.image_to_string(img_lc)
    codejj = pytesseract.image_to_string(img_jj)
    codehj = pytesseract.image_to_string(img_hj)
    # codes = pytesseract.image_to_string(img_s, lang="chi_sim")


    lastcoded = coded
    res.writelines("{}_{}_{}_{}_{}_{}\n".format(coded, codet,codeyeb,codelc,codejj,codehj))
    print("{}_{}_{}_{}_{}_{}".format(coded, codet,codeyeb,codelc,codejj,codehj))
