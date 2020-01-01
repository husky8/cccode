# coding=utf-8
import os
import time
import io
import importlib, sys

importlib.reload(sys)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from invest.getRaelValue import getStock
from tools.getSomething import getDateProperty
from invest.阿里机器人接口 import 发送消息
import configparser

robotUrl = "https://oapi.dingtalk.com/robot/send?access_token=f4d80d72e703ef2074e2e5eeada5fd930d14ba7fffb4b423c795f21928b8d6a0"

today = time.strftime('%Y%m%d', time.localtime(time.time()))
dateProperty = getDateProperty(today)

if dateProperty["worknm"] != "工作日" or int(dateProperty["week_1"]) >= 6:
    print("当天不开盘")
    exit(0)
DEBUG = False


def sendMsg(msg):
    """
    :param msgList:
    :return: 解析消息列表 并发送钉钉消息
    """
    f = open("不同步.log")
    发送消息().发送普通文本消息(msg, apiurl=robotUrl)


targetDic = [

    {"name": "交通银行", "code": "601328", "t": "4.00"},
]

for i in targetDic:
    r = getStock(i["code"])
    rp = float(r["info"]["c"])

    # 读取配置
    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.abspath(__file__)) + "/config.ini")
    lastvalue = float(config.get("stock", r["code"] + "lastValue"))

    # 判断幅度写入配置
    if lastvalue - 0.06 <= rp <= lastvalue + 0.06:
        continue
    else:
        config.set("stock", r["code"] + "lastValue", str(rp))
        config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))

    if DEBUG:
        print("【{}】今日收盘价格为【{}】成本价为【6.005】今日涨跌幅【{:.2f}%】截止今日收益为【{:.3f}%】".format(i["name"], rp, (
                float(r["info"]["c"]) / float(r["info"]["yc"]) * 100 - 100), (rp / 6.005) * 100 - 100))
    else:
        sendMsg("【{}】今日收盘价格为【{}】成本价为【6.005】今日涨跌幅【{:.2f}%】截止今日收益为【{:.3f}%】".format(i["name"], rp, (
                float(r["info"]["c"]) / float(r["info"]["yc"]) * 100 - 100), (rp / 6.005) * 100 - 100))
