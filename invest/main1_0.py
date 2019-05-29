# coding=utf-8
import sys
import os
import time
import sys
import importlib,sys
importlib.reload(sys)
import configparser

# print(sys.argv[0])
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# sys.path.append("..")
# sys.path.append(os.getcwd())
# print(os.getcwd())

from invest.useExcel import GetInfoFromExcel
from invest.useExcel import WriteDataToExcel
from invest.useExcel import CreateNewWorkbook
from invest.useExcel import ModifyExcel
from invest.getRaelValue import getStock
from tools.getSomething import getDateProperty
from invest.阿里机器人接口 import 发送消息


robotUrl = "https://oapi.dingtalk.com/robot/send?access_token=c1c7e7ee961fd1049876fe87d98cdbf6ba106cfa3a5f616333e33cbfc780db98"
def sendMsg(msg):
    """
    :param msgList:
    :return: 解析消息列表 并发送钉钉消息
    """
    f = open("不同步.log")
    发送消息().发送普通文本消息(msg, apiurl=robotUrl,atList=f.readlines())



targetDic = [
    {"name":"农业银行","code":"601288","t":"3.53"},
    {"name":"中国银行","code":"601988","t":"3.61"},
    {"name":"建设银行","code":"601939","t":"5.82"},
    {"name":"工商银行","code":"601398","t":"4.95"},
             ]

for i in targetDic:
    r = getStock(i["code"])
    rp = r["info"]["c"]
    if rp <= i["t"]:
        sendMsg("【{}】目前价格为【{}】低于目标价格【{}】可以考虑买入".format(i["name"],i["code"],i["t"]))















