import time

loglevel=0
def colorLog(text,logPath = None,fontstyle="默认",fontColor="白",backColor="无",level=None):
    """
    :param text:需要输出的文本
    :param style:默认，高亮，非粗，下划线，非下划线，闪烁，非闪烁，反显，非反显
    :param fontColor: 黑（默认），红，绿，黄，蓝，紫，青，白
    :param backColor: 黑，红，绿，黄，蓝，紫，青，白（默认）
    :return:输出文本
    """
    if logPath is None:logPath="1111.txt"
    f=open( logPath,"a",encoding="utf8")
    style={'默认': '0', '高亮': '1', '非粗': '22', '下划线': '4', '非下划线': '24', '闪烁': '5', '非闪烁': '25', '反显': '7', '非反显': '27'}
    font={'黑': ';30', '红': ';31', '绿': ';32', '黄': ';33', '蓝': ';34', '紫': ';35', '青': ';36', '白': ';37'}
    back={'无':'','黑': ';40', '红': ';41', '绿': ';42', '黄': ';43', '蓝': ';44', '紫': ';45', '青': ';46', '白': ';47'}
    if level != None:
        text=level+"||"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"||"+text+"\n"
    finalStyle=style[fontstyle]+font[fontColor]+back[backColor]
    print("\033[{}m{}\033[0m".format(finalStyle,text))
    f.writelines(text)
    f.close()
def Alarm(text,logPath=None):
    """
    :param text:
    :return:
    """

    colorLog(text,  logPath=logPath,fontColor="红", backColor="黄")

def Info(text,logPath=None):
    """
    :param text:
    :return:
    """
    if loglevel<2:
        colorLog(text, logPath=logPath,fontColor="绿",level="info")

if __name__ == '__main__':
    Info("测试颜色")