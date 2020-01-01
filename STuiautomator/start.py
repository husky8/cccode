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


res = open("res.txt", "w", encoding="utf-8")
d = u2.connect()
lastcoded = 0
xpos = 957/1080
while xpos < 0.93:
    print(xpos)
    xpos = round(xpos + 0.001, 4)
    d.click(xpos, random.randint(700, 850) / 1000)
    d.screenshot("xx.gif")
    image = Image.open('xx.gif')
    img_t = image.crop((417, 749, 670, 817))
    img_t = saveblack(img_t)

    img_ye = image.crop((250, 1100, 670, 1150))
    img_ye = saveblack(img_ye)
    img_yeb = image.crop((656, 1100, 1000, 1150))
    img_yeb = saveblack(img_yeb)
    img_lc = image.crop((250, 1170, 500, 1250))
    img_lc = saveblack(img_lc)
    img_jj = image.crop((656, 1170, 1000, 1250))
    img_jj = saveblack(img_jj)
    img_hj = image.crop((250, 1250, 500, 1300))
    img_hj = saveblack(img_hj)

    img_d = image.crop((200, 1450, 1080, 1511))
    img_d = ImageChops.invert(img_d)
    img_d = saveblack(img_d)

    # img_t.save("xx_t.gif")
    # img_ye.save("xx_ye.gif")
    # img_yeb.save("xx_yeb.gif")
    # img_lc.save("xx_lc.gif")
    # img_jj.save("xx_jj.gif")
    # img_hj.save("xx_hj.gif")
    # img_d.save("xx_d.gif")

    codet = pytesseract.image_to_string(img_t, lang="chi_sim")
    codeye = pytesseract.image_to_string(img_ye, lang="chi_sim")
    codeyeb = pytesseract.image_to_string(img_yeb, lang="chi_sim")
    codelc = pytesseract.image_to_string(img_lc, lang="chi_sim")
    codejj = pytesseract.image_to_string(img_jj, lang="chi_sim")
    codehj = pytesseract.image_to_string(img_hj, lang="chi_sim")
    coded = pytesseract.image_to_string(img_d, lang="chi_sim")
    if coded == lastcoded:
        continue
    lastcoded = coded
    res.writelines("{}_{}_{}_{}_{}_{}_{}\n".format(coded, codet, codeye,codeyeb,codelc,codejj,codehj))
    print("{}_{}_{}_{}_{}_{}_{}\n".format(coded, codet, codeye,codeyeb,codelc,codejj,codehj))
