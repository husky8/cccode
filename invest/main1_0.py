# coding=utf-8
import sys
import os
import time
import sys
import io
import importlib, sys

importlib.reload(sys)
import configparser

# print(sys.argv[0])
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# sys.path.append("..")
# sys.path.append(os.getcwd())
# print(os.getcwd())


from invest.getRaelValue import getStock
from invest.getRaelValue import getIndex
from tools.getSomething import getDateProperty
from invest.阿里机器人接口 import 发送消息

robotUrl = "https://oapi.dingtalk.com/robot/send?access_token=f4d80d72e703ef2074e2e5eeada5fd930d14ba7fffb4b423c795f21928b8d6a0"


def sendMsg(msg):
    """
    :param msgList:
    :return: 解析消息列表 并发送钉钉消息
    """
    f = open("不同步.log")
    发送消息().发送普通文本消息(msg, apiurl=robotUrl, atList=f.readlines())


targetDic = [

    {"name": "建设银行", "code": "601939", "t": "4.08"},
    {"name": "农业银行", "code": "601288", "t": "2.32"},
    {"name": "中国银行", "code": "601988", "t": "2.45"},
    {"name": "工商银行", "code": "601398", "t": "3.35"},
    {"name": "交通银行", "code": "601328", "t": "4.00"},
]

for i in targetDic:
    r = getStock(i["code"])
    rp = r["info"]["c"]
    if rp <= i["t"]:
        sendMsg("【{}】目前价格为【{}】低于目标价格【{}】可以考虑买入，预计股息率会达到7.5%".format(i["name"], i["code"], i["t"]))

indexDic = [{"name": "创业板指", "code": "399006", "t": 1470},]
for i in indexDic:

    r = getIndex(i["code"])
    rp = float(r["prePrice"])
    if rp <= i["t"]:
        sendMsg("【{}】目前价格为【{}】低于目标价格【{}】可以考虑买入,进行基金定投".format(i["name"], rp, i["t"]))
