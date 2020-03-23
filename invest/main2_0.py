# coding=utf-8
import sys
import os
import time
import sys
import importlib, sys

importlib.reload(sys)
import configparser

# print(sys.argv[0])
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import uuid
# sys.path.append("..")
# sys.path.append(os.getcwd())
# print(os.getcwd())
import json
from invest.useExcel import GetInfoFromExcel
from invest.getRaelValue import getTHHS300A
from invest.getRaelValue import getTHZZ500C
from tools.getSomething import getDateProperty
from invest.阿里机器人接口 import 发送消息
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker
from matplotlib.pyplot import MultipleLocator
import pandas as pd

DEBUG = False
mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
mac = ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
if mac in ("ac:de:48:00:11:22","00:e0:4c:71:6b:78"):
    DEBUG = True

# DEBUG=True

today = time.strftime('%Y%m%d', time.localtime(time.time()))

dateProperty = getDateProperty(today)
if (dateProperty["worknm"] != "工作日" or int(dateProperty["week_1"]) >= 6) and not DEBUG:
    print("当天不开盘")
    exit(0)

configFilePath = os.getcwd() + "/" + "配置.xlsx"
HS300REALVALUE = getTHHS300A()
ZZ500REALVALUE = getTHZZ500C()
print(HS300REALVALUE)
print(ZZ500REALVALUE)
# ModifyExcel().modifyExcel("配置.xlsx", "F1", HS300REALVALUE, "hs300")
# ModifyExcel().modifyExcel("配置.xlsx", "F1", ZZ500REALVALUE, "zz500")
robotUrl = "https://oapi.dingtalk.com/robot/send?access_token=f4d80d72e703ef2074e2e5eeada5fd930d14ba7fffb4b423c795f21928b8d6a0"

datass = (GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="hs300"))


def calculate(datass, realValue):
    keys = (datass.pop(0))  # 取出第一行为字段索引
    numberIndex = keys.index('编号')
    成本index = keys.index('成本')
    muchIndex = keys.index('份数')
    buyPriceindex = keys.index('购单价')
    targetIndex = keys.index('目标')
    # 售单价index = keys.index('售单价')
    盈利index = 7
    statusIndex = keys.index('状态')
    日志index = keys.index('日志')

    msgList = []
    saleCount = 0
    for datas in datass:

        # 盈利计算
        for i in range(len(datas)):
            try:
                datas[i] = float(datas[i])
            except:
                pass
        # print(datas)
        # print(datas[targetIndex])
        # exit(0)
        # print(type(realValue))
        # print(type(datas[buyPriceindex]))
        # print(type(datas[targetIndex]))
        if datas[statusIndex] == "持有" and DEBUG:
            print("正在计算【{}】【{}】份购买价格【{}】目前价格【{}】目前收益率【{:.2f}%】目标收益率【{:.2f}%】剩余【{:.2f}%】".format(
                datas[numberIndex], datas[muchIndex], datas[buyPriceindex], realValue,
                (realValue / datas[buyPriceindex] - 1) * 100,
                datas[targetIndex] * 100, (datas[targetIndex] - (realValue / datas[buyPriceindex] - 1)) * 100))

        if datas[statusIndex] == "持有" and realValue > datas[buyPriceindex] * (1 + float(datas[targetIndex])):
            msg = "编号为【{编号}】的【{份数}】份基金目前收益率【{当前收益率:.2f}%】超过计划收益率【{目标:.2f}%】可售出".format(
                编号=datas[numberIndex],
                份数=datas[muchIndex],
                当前收益率=(realValue / datas[buyPriceindex] - 1) * 100,
                目标=datas[targetIndex] * 100,
            )
            saleCount = saleCount + datas[muchIndex]

            msgList.append(msg)
            continue
    if saleCount != 0:
        msgList.append("合计应出售【{合计出售份数:.2f}】份".format(合计出售份数=saleCount))

        # 合并计算
        if datas[statusIndex] == "持有" and realValue < datas[buyPriceindex] * (1 - 1.5 * datas[targetIndex]):
            # if True:
            msg = "编号为【{编号}】的【{份数}】份基金目前收益率【{当前收益率:.2f}%】请考虑合并".format(
                编号=datas[numberIndex],
                份数=datas[muchIndex],
                当前收益率=(realValue / datas[buyPriceindex] - 1) * 100,
                目标=datas[targetIndex] * 100,
            )
            # print(msg)
            msgList.append(msg)
    return msgList


def getchartdatas(datass, realValue, mark=""):
    keys = (datass.pop(0))  # 取出第一行为字段索引
    numberIndex = keys.index('编号')
    成本index = keys.index('成本')
    收益index = keys.index('成本')
    buyPriceindex = keys.index('购单价')
    targetIndex = keys.index('目标')
    statusIndex = keys.index('状态')
    targetchartdatas = []
    pointColor = {"HS300": ["#2786ba", "#cc0000"], "ZZ500": ["#40bfd2", "#ff0000"]}
    for datas in datass:

        # 盈利计算
        for i in range(len(datas)):
            try:
                datas[i] = float(datas[i])
            except:
                pass
        # temp = realValue / datas[buyPriceindex] - 1 # 查看当前收益状态
        temp = realValue / datas[buyPriceindex] - 1 - datas[targetIndex]
        isHave = True if datas[statusIndex] == "持有" else False
        targetchartdatas.append(
            {"date": datas[numberIndex][-6:], "value": temp if isHave else 0.03 if mark == "HS300" else 0.05,
             "rank": datas[成本index], "pointColor": pointColor[mark][0] if isHave else pointColor[mark][1]})
    return targetchartdatas


def gettargetimg():
    imgpath = "log/{}.png".format(today) if DEBUG else r"C:\Users\Administrator\cccloud\static\bondscatter\{}.png".format(
        today)

    HS300chartdatas = getchartdatas(GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="hs300"),
                                    HS300REALVALUE, "HS300")
    HS300pd = pd.DataFrame(HS300chartdatas)
    ZZ500chartdatas = getchartdatas(GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="zz500"),
                                    ZZ500REALVALUE, "ZZ500")
    ZZ500pd = pd.DataFrame(ZZ500chartdatas)
    # print(ZZ500pd)
    plt.figure(figsize=(2, 1))
    plt.rcParams['savefig.dpi'] = 300
    fig, ax = plt.subplots()
    ax.scatter(HS300pd["date"], HS300pd["value"], linewidths=HS300pd["rank"] / 75, c=HS300pd["pointColor"], marker='.')
    ax.scatter(ZZ500pd["date"], ZZ500pd["value"], linewidths=ZZ500pd["rank"] / 75, c=ZZ500pd["pointColor"], marker='.')
    ax.plot(ZZ500pd["date"], [0.0005 for i in range(len(ZZ500pd["date"]))], c="#d82626", linewidth=1)
    ax.plot(ZZ500pd["date"], [-0.0005 for i in range(len(ZZ500pd["date"]))], c="#009900", linewidth=1)
    # ax.legend(["HS300","ZZ500"])
    ax.text(0.5, 1.05, "{} bond target status".format(today), transform=ax.transAxes, color='#333333', size=20,
            ha='center', weight=100)
    ax.grid(which='major', axis='y', linestyle='-')
    ax.yaxis.set_major_locator(MultipleLocator(0.025))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    ax.margins(0, 0.01)
    # plt.xticks([])
    plt.xticks(rotation=45)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
    # ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    plt.savefig(imgpath)
    # print(min(HS300pd["value"].min(),ZZ500pd["value"].min()))
    print("make img success ~")


def to_percent(temp, position):
    return '%.1f' % (100 * temp) + '%'


def sendMsg(msgList):
    """
    :param msgList:
    :return: 解析消息列表 并发送钉钉消息
    """
    f = open("不同步.log")
    finMsg = ""
    for msg in msgList:
        finMsg = finMsg + msg + "\n"
    发送消息().发送普通文本消息(finMsg, apiurl=robotUrl, atList=f.readlines())


if __name__ == '__main__':
    if DEBUG:
        gettargetimg()
    if not DEBUG:
        if int(dateProperty["week_1"]) % 2 == 0:
            gettargetimg()
            发送消息().发送整体跳转消息(robotUrl, "未出售基金目标达成趋势.", "https://cccloud.xyz/static/bondscatter/{}.png".format(today),
                            singleTitle="{} bond target status".format(today),
                            singleURL="https://cccloud.xyz/static/bondscatter/{}.png".format(today))
            time.sleep(10)
    datass = (GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="hs300"))
    msgList = calculate(datass, HS300REALVALUE)
    if DEBUG:
        print(json.dumps(msgList,ensure_ascii=False)  if msgList != [] else "沪深300无结果")
    if not DEBUG:
        if msgList != []: sendMsg(msgList)

    datass = (GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="zz500"))
    # ZZ500REALVALUE = ZZ500REALVALUE*1.05
    msgList = calculate(datass, ZZ500REALVALUE)
    if DEBUG:
        print(len(msgList))
        print(json.dumps(msgList,ensure_ascii=False) if msgList != [] else "中证500无结果")
    if not DEBUG:
        if msgList != []: sendMsg(msgList)
