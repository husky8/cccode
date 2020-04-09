# coding=utf-8
import sys
import os
import time
import datetime
import io
import importlib
import uuid

importlib.reload(sys)
import configparser

sys.path.append(r"C:\Users\Administrator\cccode\cccode")
# print(sys.argv[0])
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from invest.getRaelValue import getNewStock
from tools.DT import get_day_property
from tools.DT import getMarketDayDiff
from invest.阿里机器人接口 import 发送消息
import configparser

config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + "/config.ini")
robotUrl = config.get("dingdingUrl", "hjbf")
ZZLURL = config.get("dingdingUrl", "zzlurl")
ZHURL = config.get("dingdingUrl", "zhkzz")
ccphone = config.get("phone", "cc")
zsqphone = config.get("phone", "zsq")
zzlphone = config.get("phone", "zzl")
zhphone = config.get("phone", "zh")

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# today = "2020-01-10"
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
mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
mac = ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
if mac == "ac:de:48:00:11:22":
    DEBUG = True

# DEBUG=False

RETRYTIMES = 0
HAVEINGLIST = {
    "113574": {"name": "利群转债", "atList": [zsqphone]},
    "110067": {"name": "华安转债", "atList": [zsqphone,zhphone]},
    "128102": {"name": "海大转债", "atList": [ccphone]},
    "110068": {"name": "龙净转债", "atList": [zsqphone]},

}


def sendMsg(msg, apiurl="default", atList="all"):
    """
    :param msgList:
    :return: 解析消息列表 并发送钉钉消息
    """
    if apiurl == "default":
        apiurl = robotUrl
    print(apiurl)
    发送消息().发送普通文本消息(msg, apiurl, isAtAll=True if atList == "all" else False,
                    atList=atList if atList != "all" else [])


def checkBond():
    # today = "2020-04-10"
    bondlist = getNewStock("bond")
    if type(bondlist) != type([1, 2, 3]):

        if DEBUG:
            print(bondlist)
            pass
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

        if bond["BONDCODE"] in HAVEINGLIST.keys() and bond["LISTDATE"] != "-":
            saleDay = datetime.datetime.strptime(bond["LISTDATE"][:10], '%Y-%m-%d').date()
            todayDate = datetime.datetime.strptime(today, '%Y-%m-%d').date()
            print(today,saleDay)
            if todayDate <= saleDay:
                saleRes.append({"code": bond["BONDCODE"], "name": bond["SNAME"], "saleDay": saleDay})

    if applyRes != []:
        applyRes = "、".join(applyRes)
        if DEBUG:
            print("今日有可转债【{}】申购，请查看溢价率及评估市场行情后申购".format(applyRes))
        else:
            sendMsg("今日有可转债【{}】申购，请查看溢价率及评估市场行情后申购".format(applyRes), atList=[ccphone, zsqphone])
            sendMsg("今日有可转债【{}】申购，请查看溢价率及评估市场行情后申购".format(applyRes), apiurl=ZZLURL)
            sendMsg("今日有可转债【{}】申购，请查看溢价率及评估市场行情后申购".format(applyRes), apiurl=ZHURL)

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
            sendMsg("T-2日有可转债【{}】申购，如申购，请及时查看是否中签，预留预缴款".format(checkRes), atList=[ccphone, zsqphone])
            sendMsg("T-2日有可转债【{}】申购，如申购，请及时查看是否中签，预留预缴款".format(checkRes), apiurl=ZZLURL)
            sendMsg("T-2日有可转债【{}】申购，如申购，请及时查看是否中签，预留预缴款".format(checkRes), apiurl=ZHURL)

    if saleRes != []:
        for i in saleRes:
            if DEBUG:
                print("你持仓的【{}】，{}上市交易，请注意择机出售 {}".format(i["name"], "将于【{}】".format(i["saleDay"]) if str(
                    i["saleDay"]) != today else "已于【今日】", HAVEINGLIST[i["code"]]['atList']))
            else:
                if ccphone in HAVEINGLIST[i["code"]]['atList'] or zsqphone in HAVEINGLIST[i["code"]]['atList'] :
                    sendMsg("你持仓的【{}】，{}上市交易，请注意择机出售".format(i["name"], "将于【{}】".format(i["saleDay"]) if str(
                        i["saleDay"]) != today else "已于【今日】"), atList=HAVEINGLIST[i["code"]]['atList'])
                if zzlphone in HAVEINGLIST[i["code"]]['atList']:
                    sendMsg("你持仓的【{}】，{}上市交易，请注意择机出售".format(i["name"], "将于【{}】".format(i["saleDay"]) if str(
                        i["saleDay"]) != today else "已于【今日】"), apiurl=ZZLURL,atList=[zzlphone])
                if zhphone in HAVEINGLIST[i["code"]]['atList']:
                    sendMsg("你持仓的【{}】，{}上市交易，请注意择机出售".format(i["name"], "将于【{}】".format(i["saleDay"]) if str(
                        i["saleDay"]) != today else "已于【今日】"), apiurl=ZHURL,atList=[zhphone])


def checkIpo():
    # today = "2020-01-06"
    # todayDiff_2 = "2020-01-06"
    ipolist = getNewStock("ipo")
    print(ipolist)
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
        print(ipo)
        # print(ipo["purchasedate"])
        # print(today in ipo["purchasedate"])
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
            # print("今日有【{}】新股申购".format(applyRes))
            pass
        else:
            sendMsg("今日有【{}】新股申购".format(applyRes))
    if checkRes != []:
        checkRes = "、".join(checkRes)
        if DEBUG:
            print("T-2日有【{}】新股申购,请及时查看是否中签，预留预缴款".format(checkRes))
            pass
        else:
            sendMsg("T-2日有【{}】新股申购,请及时查看是否中签，预留预缴款".format(checkRes))


if __name__ == '__main__':
    checkBond()
    checkIpo()
