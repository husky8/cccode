# coding=utf-8
import sys
import os
import time
import sys
import importlib, sys
import datetime

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
from tools.DT import get_day_property

DEBUG = False
mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
mac = ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
if mac in ("ac:de:48:00:11:22", "00:e0:4c:71:6b:78","a6:83:e7:52:66:d7"):
    DEBUG = True

# DEBUG=False

today = time.strftime('%Y%m%d', time.localtime(time.time()))

dateProperty = get_day_property(today)
if not dateProperty["data"]["workday"] or dateProperty["data"]["weekday"] >= 6:
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
        # print(datas)
        # 盈利计算
        for i in range(len(datas)):
            try:
                datas[i] = float(datas[i])
            except:
                pass
        # temp = realValue / datas[buyPriceindex] - 1 # 查看当前收益状态
        # isHave = True if datas[statusIndex] == "持有" else False
        # targetchartdatas.append(
        #     {"date": datas[numberIndex][-6:], "value": float(datas[statusIndex-1]) / datas[成本index] ,
        #      "rank": datas[成本index], "pointColor": pointColor[mark][0] if isHave else pointColor[mark][1]})

        temp = realValue / datas[buyPriceindex] - 1 - datas[targetIndex]
        isHave = True if datas[statusIndex] == "持有" else False
        targetchartdatas.append(
            {"date": datas[numberIndex][-6:], "value": temp if isHave else 0.03 if mark == "HS300" else 0.05,
             "rank": datas[成本index], "pointColor": pointColor[mark][0] if isHave else pointColor[mark][1]})

    return targetchartdatas


def gettargetimg():
    imgpath = "log/{}.png".format(
        today) if DEBUG else r"C:\cccloud\static\bondscatter\{}.png".format(
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


def checkRange():
    from invest.getRaelValue import getIndex
    cur_day = datetime.datetime(2015, 6, 10)
    next_day = datetime.datetime.today()
    upvalue = 1.05 ** ((next_day - cur_day).days / 365)
    this300value = float(getIndex(399300)["details"][-1].split(",")[1])
    this500value = float(getIndex(399905)["details"][-1].split(",")[1])

    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.abspath(__file__)) + "/config.ini")
    now300target = config.get("RegularInvestment", "hs300")
    now500target = config.get("RegularInvestment", "zz500")

    if DEBUG:
        print("-" * 66)
        print("Years Up Value is {:.2f}%".format(100 * upvalue))
        print("-"*66)
        print("highest  HS300 is 5300")
        print("This 300 Value is {}".format(this300value))
        print("Now 300 target is {}".format(now300target))
        if now300target == "TOP":
            print("Higt 300 Value is {}".format(round(5300 * upvalue * 0.75, 2)))
            print("Higt 300 Range is {:.2f}%".format(100 * (1 - this300value / round(5300 * upvalue * 0.75, 2))))
        elif now300target == "LOW":
            print("Low 300 Value is {}".format(round(5300 * upvalue * 0.75 * 0.85, 2)))
            print("Low 300 Range is {:.2f}%".format(100 * (1 - this300value / round(5300 * upvalue * 0.75 * 0.9, 2))))
        print("-" * 66)
        print("highest  ZZ500 is 11000")
        print("This 500 Value is {}".format(this500value))
        print("Now 500 target is {}".format(now500target))
        if now500target == "TOP":
            print("Higt 500 Value is {}".format(round(11000 * upvalue * 0.65, 2)))
            print("Higt 500 Range is {:.2f}%".format(100 * (1 - this500value / round(11000 * upvalue * 0.65, 2))))
        elif now500target == "LOW":
            print("Low 500 Value is {}".format(round(11000 * upvalue * 0.65 * 0.85, 2)))
            print("Low 500 Range is {:.2f}%".format(100 * (1 - this500value / round(11000 * upvalue * 0.65 * 0.9, 2))))


        if now300target == "TOP" and this300value > 5300 * upvalue * 0.75:
            print(["沪深300已到达【停止】定投限制 请确认后【修改定投计划为每笔10元】见好就收鸭~", ])
            config.set("RegularInvestment", "hs300", "LOW")
            config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))

        if now500target == "TOP" and this500value > 11500 * upvalue * 0.65:
            print(["中证500已到达【停止】定投限制 请确认后【修改定投计划为每笔10元】见好就收鸭~", ])
            config.set("RegularInvestment", "zz500", "LOW")
            config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))

        if now300target == "LOW" and this300value < 5300 * upvalue * 0.75 * 0.85:
            print(["沪深300已到达【开启】定投限制 请确认后【修改定投计划为每笔150元】祝好运喽~", ])
            config.set("RegularInvestment", "hs300", "TOP")
            config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))

        if now500target == "LOW" and this500value < 11500 * upvalue * 0.65 * 0.85:
            print(["中证500已到达【开启】定投限制 请确认后【修改定投计划为每笔150元】祝好运喽~", ])
            config.set("RegularInvestment", "zz500", "TOP")
            config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))
    else:
        if now300target == "TOP" and this300value > 5300 * upvalue * 0.75 :
            sendMsg(["沪深300已到达【停止】定投限制 请确认后【修改定投计划为每笔10元】见好就收鸭~", ])
            config.set("RegularInvestment", "hs300", "LOW")
            config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))

        if now500target == "TOP" and this500value > 11500 * upvalue * 0.65 :
            sendMsg(["中证500已到达【停止】定投限制 请确认后【修改定投计划为每笔10元】见好就收鸭~", ])
            config.set("RegularInvestment", "zz500", "LOW")
            config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))

        if now300target == "LOW" and this300value < 5300 * upvalue * 0.7 * 0.85:
            sendMsg(["沪深300已到达【开启】定投限制 请确认后【修改定投计划为每笔150元】祝好运喽~", ])
            config.set("RegularInvestment", "hs300", "TOP")
            config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))

        if now500target == "LOW" and this500value < 11500 * upvalue * 0.6 * 0.85:
            sendMsg(["中证500已到达【开启】定投限制 请确认后【修改定投计划为每笔150元】祝好运喽~", ])
            config.set("RegularInvestment", "zz500", "TOP")
            config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))


if __name__ == '__main__':

    if DEBUG:
        gettargetimg()
    if not DEBUG:
        config = configparser.ConfigParser()
        config.read(os.path.dirname(os.path.abspath(__file__)) + "/config.ini")
        now300target = config.get("RegularInvestment", "hs300")
        now500target = config.get("RegularInvestment", "zz500")
        if True:#int(dateProperty["week_1"]) % 2 == 0:
            gettargetimg()
            发送消息().发送链接文本消息(robotUrl, "未出售基金目标达成趋势.",
                            "沪深300检测目标为{}\n中证500检测目标为{}".format(now300target,now500target),
                            picUrl="https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00744-1952.jpg",
                            messageUrl="https://81.70.153.8/static/bondscatter/{}.png".format(today)
                            )
            time.sleep(10)
    datass = (GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="hs300"))
    msgList = calculate(datass, HS300REALVALUE)
    if DEBUG:
        print(len(msgList) - 1)
        print(json.dumps(msgList, ensure_ascii=False) if msgList != [] else "沪深300无结果")
    if not DEBUG:
        if msgList != []: sendMsg(msgList)

    datass = (GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="zz500"))
    # ZZ500REALVALUE = ZZ500REALVALUE*1.05
    msgList = calculate(datass, ZZ500REALVALUE)
    if DEBUG:
        print(len(msgList) - 1)
        print(json.dumps(msgList, ensure_ascii=False) if msgList != [] else "中证500无结果")
    if not DEBUG:
        if msgList != []: sendMsg(msgList)
    checkRange()
