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
if mac in ("ac:de:48:00:11:22", "00:e0:4c:71:6b:78", "a6:83:e7:52:66:d7"):
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
    if saleCount != 0:
        msgList.append("合计应出售【{合计出售份数:.2f}】份".format(合计出售份数=saleCount))
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


def sendMsgOrPrint(msgList):
    if DEBUG:
        print(msgList)
    else:
        sendMsg(msgList)


def checkRange():
    from invest.getRaelValue import getIndex
    cur_day = datetime.datetime.today()
    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.abspath(__file__)) + "/config.ini")

    # 历史最高日期,历史最高指数,最近最高日期,最近最高指数,时间加权，人工微调加权，检测方向
    hs300HistoryTopDate = datetime.datetime.strptime(config.get("RegularInvestment", "hs300HistoryTopDate"), '%Y-%m-%d')
    zz500HistoryTopDate = datetime.datetime.strptime(config.get("RegularInvestment", "zz500HistoryTopDate"), '%Y-%m-%d')
    hs300HistoryTopIndex = float(config.get("RegularInvestment", "hs300HistoryTopIndex"))
    zz500HistoryTopIndex = float(config.get("RegularInvestment", "zz500HistoryTopIndex"))
    hs300LastTopDate = datetime.datetime.strptime(config.get("RegularInvestment", "hs300LastTopDate"), '%Y-%m-%d')
    zz500LastTopDate = datetime.datetime.strptime(config.get("RegularInvestment", "zz500LastTopDate"), '%Y-%m-%d')
    hs300LastTopIndex = float(config.get("RegularInvestment", "hs300LastTopIndex"))
    zz500LastTopIndex = float(config.get("RegularInvestment", "zz500LastTopIndex"))
    hs300HistoryUpValue = round(1.05 ** ((cur_day - hs300HistoryTopDate).days / 365), 4)
    zz500HistoryUpValue = round(1.05 ** ((cur_day - zz500HistoryTopDate).days / 365), 4)
    hs300LastUpValue = round(1.05 ** ((cur_day - hs300LastTopDate).days / 365), 4)
    zz500LastUpValue = round(1.05 ** ((cur_day - zz500LastTopDate).days / 365), 4)

    hs300Adjust = float(config.get("RegularInvestment", "hs300Adjust"))
    zz500Adjust = float(config.get("RegularInvestment", "zz500Adjust"))
    now300target = config.get("RegularInvestment", "hs300")
    now500target = config.get("RegularInvestment", "zz500")

    now300value = float(getIndex(399300)["details"][-1].split(",")[1])
    now500value = float(getIndex(399905)["details"][-1].split(",")[1])

    hs300StopPoint = round(hs300HistoryTopIndex * hs300HistoryUpValue * hs300Adjust * 0.75, 2)  # 微调后,到达历史最高 75% 停止
    zz500StopPoint = round(zz500HistoryTopIndex * zz500HistoryUpValue * zz500Adjust * 0.75, 2)
    hs300StartPoint = round(hs300LastTopIndex * hs300LastUpValue * 0.8, 2)  # 到达最近最高 80% 开始
    zz500StartPoint = round(zz500LastTopIndex * zz500LastUpValue * 0.8, 2)

    if DEBUG:
        print("现在300方向", now300target)
        print("现在500方向", now500target)
        print("现在300", now300value)
        print("现在500", now500value)
        print("300开始", hs300StartPoint)
        print("300结束", hs300StopPoint)
        print("500开始", zz500StartPoint)
        print("500结束", zz500StopPoint)

    # hs300
    # 触发关闭 并 更新近高
    if now300target == "TOP" and now300value > hs300StopPoint:
        config.set("RegularInvestment", "hs300", "LOW")
        config.set("RegularInvestment", "hs300LastTopIndex", str(now300value))
        config.set("RegularInvestment", "hs300LastTopDate", str(datetime.date.today()))
        config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))
        sendMsgOrPrint(["沪深300已到达【关闭】定投限制 请确认后【修改定投计划为每笔10元】见好就收鸭~", ])
    # 触发开启
    if now300target == "LOW" and now300value < hs300StartPoint:
        config.set("RegularInvestment", "hs300", "TOP")
        config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))
        sendMsgOrPrint(["沪深300已到达【开启】定投限制 请确认后【修改定投计划为每笔150元】祝你好运喽~", ])
    # 更新进高
    if now300target == "LOW" and now300value > hs300LastTopIndex:
        config.set("RegularInvestment", "hs300LastTopIndex", str(now300value))
        config.set("RegularInvestment", "hs300LastTopDate", str(datetime.date.today()))
        config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))
        sendMsgOrPrint(["沪深300已超过最近新高 现在 {} 近期最高 {}".format(now300value, hs300LastTopIndex), ])
    # 更新最高
    if now300value > hs300HistoryTopIndex:
        config.set("RegularInvestment", "hs300HistoryTopIndex", str(now300value))
        config.set("RegularInvestment", "hs300HistoryTopDate", str(datetime.date.today()))
        config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))
        sendMsgOrPrint(["沪深300已超过历史新高 现在 {} 历史最高 {}".format(now300value, hs300HistoryTopIndex), ])

    # zz500
    # 触发关闭 并 更新近高
    if now500target == "TOP" and now500value > zz500StopPoint:
        config.set("RegularInvestment", "zz500", "LOW")
        config.set("RegularInvestment", "zz500LastTopIndex", str(now500value))
        config.set("RegularInvestment", "zz500LastTopDate", str(datetime.date.today()))
        config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))
        sendMsgOrPrint(["沪深500已到达【关闭】定投限制 请确认后【修改定投计划为每笔10元】见好就收鸭~", ])
    # 触发开启
    if now500target == "LOW" and now500value < zz500StartPoint:
        config.set("RegularInvestment", "zz500", "TOP")
        config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))
        sendMsgOrPrint(["沪深500已到达【开启】定投限制 请确认后【修改定投计划为每笔150元】祝你好运喽~", ])
    # 更新进高
    if now500target == "LOW" and now500value > zz500LastTopIndex:
        config.set("RegularInvestment", "zz500LastTopIndex", str(now500value))
        config.set("RegularInvestment", "zz500LastTopDate", str(datetime.date.today()))
        config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))
        sendMsgOrPrint(["沪深500已超过最近新高 现在 {} 近期最高 {}".format(now500value, zz500LastTopIndex), ])
    # 更新最高
    if now500value > zz500HistoryTopIndex:
        config.set("RegularInvestment", "zz500HistoryTopIndex", str(now500value))
        config.set("RegularInvestment", "zz500HistoryTopDate", str(datetime.date.today()))
        config.write(open(os.path.dirname(os.path.abspath(__file__)) + "/config.ini", "r+"))
        sendMsgOrPrint(["沪深500已超过历史新高 现在 {} 历史最高 {}".format(now500value, zz500HistoryTopIndex), ])


if __name__ == '__main__':

    if DEBUG:
        gettargetimg()
    if not DEBUG:
        config = configparser.ConfigParser()
        config.read(os.path.dirname(os.path.abspath(__file__)) + "/config.ini")
        now300target = config.get("RegularInvestment", "hs300")
        now500target = config.get("RegularInvestment", "zz500")
        if True:  # int(dateProperty["week_1"]) % 2 == 0:
            gettargetimg()
            发送消息().发送链接文本消息(robotUrl, "未出售基金目标达成趋势.",
                            "沪深300检测目标为{}\n中证500检测目标为{}".format(now300target, now500target),
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
