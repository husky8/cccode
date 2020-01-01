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

robotUrl = "https://oapi.dingtalk.com/robot/send?access_token=f4d80d72e703ef2074e2e5eeada5fd930d14ba7fffb4b423c795f21928b8d6a0"


today = time.strftime('%Y%m%d', time.localtime(time.time()))
dateProperty = getDateProperty(today)
if dateProperty["worknm"] != "工作日" or  int(dateProperty["week_1"]) >= 6:
    print("当天不开盘")
    exit(0)



def sendMsg(msg,atList):
    """
    :param msgList:
    :return: 解析消息列表 并发送钉钉消息
    """
    f = open("不同步.log")
    发送消息().发送普通文本消息(msg, apiurl=robotUrl,atList=atList)


targetDic = [

    {"name": "上证指数", "code": "000001"},
]

for i in targetDic:
    r = getStock(i["code"])
    rp = r["info"]["c"]


    # sendMsg("今日股票收盘结果为【{}】如果猜对了，就去支付宝换🧧吧".format("涨📈" if r["info"]["c"] > r["info"]["yc"] else "跌📉"),atList = [18888873474,])
    # print("今日股票收盘结果为【{}】如果猜对了，就去支付宝换🧧吧".format("涨📈" if r["info"]["c"] > r["info"]["yc"] else "跌📉"))

if int(dateProperty["week_1"]) == 1:
    sendMsg("基金入账",[18888851041,])
