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
    # print(r.text)
    return eval(r.text)["data"]

def getDateProperty(date):
    """
    support :https://www.nowapi.com/api/life.workday
    :param date: date  yyyymmdd
    :return: Property
    ps  "worknm": 假日/工作日,  "week_1": "4", /*星期样式1*/
    """
    r=requests.get("http://api.k780.com/?app=life.workday&date={}&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json".format(date))
    return eval(r.text)["result"]
if __name__ == '__main__':

    s = getDateProperty("20190203")
    print(s["worknm"])