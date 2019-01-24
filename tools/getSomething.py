import random
import requests

def getRandomColor():
    '''获取一个随机颜色(r,g,b)格式的'''
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)

def getRandomStr():
    '''获取一个随机字符串，每个字符的颜色也是随机的'''
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upper_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
    return random_char

def getIpAddress(ip):
    """
    :param ip: ipAddress
    :return:
    """
    r=requests.get("http://ip.taobao.com/service/getIpInfo.php?ip="+ip)
    print(r.text)
    return eval(r.text)["data"]

if __name__ == '__main__':
    getIpAddress("36.110.48.247")