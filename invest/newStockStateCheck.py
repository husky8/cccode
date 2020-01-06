# coding=utf-8
import sys
import os
import time
import datetime
import io
import importlib

importlib.reload(sys)
import configparser
sys.path.append(r"C:\Users\Administrator\cccode\cccode")
# print(sys.argv[0])
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# sys.path.append("..")
# sys.path.append(os.getcwd())
# print(os.getcwd())

from invest.getRaelValue import getNewStock
from tools.DT import get_day_property
from tools.DT import getMarketDayDiff
from invest.阿里机器人接口 import 发送消息

robotUrl = "https://oapi.dingtalk.com/robot/send?access_token=f4d80d72e703ef2074e2e5eeada5fd930d14ba7fffb4b423c795f21928b8d6a0"

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# today = "2019-06-18"
todayDiff_1 = getMarketDayDiff(today, diff=-1)
todayDiff_1 = todayDiff_1[:4] + "-" + todayDiff_1[4:6] + "-" + todayDiff_1[6:]
todayDiff_2 = getMarketDayDiff(today, diff=-2)
todayDiff_2 = todayDiff_2[:4] + "-" + todayDiff_2[4:6] + "-" + todayDiff_2[6:]

dateProperty = get_day_property(today)
# print(dateProperty)
if not dateProperty["data"]["workday"] or 5 <= int(dateProperty["data"]["weekday"]):
    print("当天不开盘")
    exit(0)

DEBUG = False
RETRYTIMES = 0
HAVEINGLIST = ["先导转债","明阳转债","木森转债","振德转债","建工转债","日月转债","深南转债","麦米转债","汽模转2","唐人转债","璞泰转债","希望转债","百川转债","乐普转债"]


def sendMsg(msg, apiurl="default"):
    """
    :param msgList:
    :return: 解析消息列表 并发送钉钉消息
    """
    if apiurl == "default":
        apiurl = robotUrl
    print(apiurl)
    发送消息().发送普通文本消息(msg, apiurl, isAtAll=True)


def checkBond():
    ZZLRURL = "https://oapi.dingtalk.com/robot/send?access_token=dce87ebd6cab4755e26a2ad2e33e6eeb7b02e5b92f9ce8f130cdf58093049ec0"
    # today = "2019-11-20"
    bondlist = getNewStock("bond")
    # print(bondlist)
    # print(todayDiff_2)
    if type(bondlist) != type([1, 2, 3]):

        if DEBUG:
            print(bondlist)
        else:
            sendMsg(bondlist)
        exit(0)
    applyRes = []
    checkRes = []
    saleRes = []
    searchRes = []
    for bond in bondlist:
        # print(bond["SNAME"])
        if today in bond["STARTDATE"]:
            applyRes.append(bond["SNAME"])
        # if todayDiff_1 in bond["STARTDATE"]:
        #     searchRes.append(bond["SNAME"])
        if todayDiff_2 in bond["STARTDATE"]:
            # print(todayDiff_2)
            checkRes.append(bond["SNAME"])

        if bond["SNAME"] in HAVEINGLIST and bond["LISTDATE"] != "-":
            saleDay = datetime.datetime.strptime(bond["LISTDATE"][:10], '%Y-%m-%d').date()
            todayDate = datetime.datetime.strptime(today, '%Y-%m-%d').date()
            # print(today,saleDay)
            if todayDate <= saleDay:
                saleRes.append({"name": bond["SNAME"], "saleDay": saleDay})

    if applyRes != []:
        applyRes = "、".join(applyRes)
        if DEBUG:
            print("今日有可转债【{}】申购，请查看溢价率及评估市场行情后申购".format(applyRes))
        else:
            sendMsg("今日有可转债【{}】申购，请查看溢价率及评估市场行情后申购".format(applyRes))
            sendMsg("今日有可转债【{}】申购，请查看溢价率及评估市场行情后申购".format(applyRes), apiurl=ZZLRURL)

    # if searchRes != []:
    #     searchRes = "、".join(searchRes)
    #     if DEBUG:
    #         print("T-1日有可转债【{}】申购，如有时间，可将申购截图发给陈程，以便提前查询是否中签".format(searchRes))
    #     else:
    #         sendMsg("T-1日有可转债【{}】申购，如有时间，可将申购截图发给陈程，以便提前查询是否中签".format(searchRes))

    if checkRes != []:
        checkRes = "、".join(checkRes)
        if DEBUG:
            print("T-2日有可转债【{}】申购，如申购，请及时查看是否中签，预留预缴款".format(checkRes))
        else:
            sendMsg("T-2日有可转债【{}】申购，如申购，请及时查看是否中签，预留预缴款".format(checkRes))
            sendMsg("T-2日有可转债【{}】申购，如申购，请及时查看是否中签，预留预缴款".format(checkRes), apiurl=ZZLRURL)

    if saleRes != []:
        for i in saleRes:
            if DEBUG:
                print("你持仓的【{}】，{}上市交易，请注意择机出售".format(i["name"], "将于【{}】".format(i["saleDay"]) if str(i["saleDay"])!=today else "已于【今日】"))
            else:
                sendMsg("你持仓的【{}】，{}上市交易，请注意择机出售".format(i["name"], "将于【{}】".format(i["saleDay"]) if str(i["saleDay"])!=today else "已于【今日】"))
                sendMsg("你持仓的【{}】，将于【{}】上市交易，请注意择机出售".format(i["name"], i["saleDay"]), apiurl=ZZLRURL)


def checkIpo():
    # today = "2019-06-18"

    ipolist = getNewStock("ipo")
    # print(ipolist)
    if type(ipolist) != type([1, 2, 3]):

        if DEBUG:
            print(ipolist)
        else:
            sendMsg(ipolist)
        exit(0)
    applyRes = []
    checkRes = []

    SZFLAG = False  # 暂时不检测深圳市场的新股
    SHFLAG = True
    for ipo in ipolist:
        # print(ipo)
        if today in ipo["purchasedate"]:

            malltype = ""
            if ipo["securitycode"][0] == "3" and SZFLAG:
                malltype = "深市创业板"
            elif ipo["securitycode"][0] == "0" and SZFLAG:
                malltype = "深市主板"
            elif ipo["securitycode"][0:2] == "68" and SHFLAG and False:
                malltype = "沪市科创板"
            elif ipo["securitycode"][0:2] == "60" and SHFLAG:
                malltype = "沪市主板"
            if malltype != "":
                applyRes.append(malltype + "的" + ipo["securityshortname"])
        if todayDiff_2 in ipo["purchasedate"]:
            malltype = ""
            if ipo["securitycode"][0] == "3" and SZFLAG:
                malltype = "深市创业板"
            elif ipo["securitycode"][0] == "0" and SZFLAG:
                malltype = "深市主板"
            elif ipo["securitycode"][0:2] == "68" and SHFLAG and False:
                malltype = "沪市科创板"
            elif ipo["securitycode"][0:2] == "60" and SHFLAG:
                malltype = "沪市主板"
            if malltype != "":
                checkRes.append(malltype + "的" + ipo["securityshortname"])
    if applyRes != []:
        applyRes = "、".join(applyRes)
        if DEBUG:
            print("今日有【{}】新股申购".format(applyRes))
        else:
            sendMsg("今日有【{}】新股申购".format(applyRes))
    if checkRes != []:
        checkRes = "、".join(checkRes)
        if DEBUG:
            print("T-2日有【{}】新股申购,请及时查看是否中签，预留预缴款".format(checkRes))
        else:
            sendMsg("T-2日有【{}】新股申购,请及时查看是否中签，预留预缴款".format(checkRes))


if __name__ == '__main__':
    checkBond()
    checkIpo()
