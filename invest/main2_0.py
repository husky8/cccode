# coding=utf-8
import sys
import os
import time
import sys
import importlib,sys
importlib.reload(sys)

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
from invest.getRaelValue import getTHHS300A
from invest.getRaelValue import getTHZZ500C
from tools.getSomething import getDateProperty
from invest.阿里机器人接口 import 发送消息

today = time.strftime('%Y%m%d', time.localtime(time.time()))
dateProperty = getDateProperty(today)
if dateProperty["worknm"] != "工作日" or  int(dateProperty["week_1"]) >= 6:
    print("当天不开盘")
    exit(0)

configFilePath =os.getcwd()+"/"+"配置.xlsx"
HS300REALVALUE=getTHHS300A()
ZZ500REALVALUE=getTHZZ500C()
print(HS300REALVALUE)
print(ZZ500REALVALUE)
# ModifyExcel().modifyExcel("配置.xlsx", "F1", HS300REALVALUE, "hs300")
# ModifyExcel().modifyExcel("配置.xlsx", "F1", ZZ500REALVALUE, "zz500")
robotUrl = "https://oapi.dingtalk.com/robot/send?access_token=c1c7e7ee961fd1049876fe87d98cdbf6ba106cfa3a5f616333e33cbfc780db98"

datass=(GetInfoFromExcel().getInfoFromExcel(configFilePath,sheetName="hs300"))
def calculate(datass,realValue):
    keys=(datass.pop(0)) #取出第一行为字段索引
    numberIndex = keys.index('编号')
    成本index = keys.index('成本')
    muchIndex = keys.index('份数')
    buyPriceindex = keys.index('购单价')
    targetIndex = keys.index('目标')
    # 售单价index = keys.index('售单价')
    盈利index = 7
    statusIndex = keys.index('状态')
    日志index = keys.index('日志')

    msgList=[]
    saleCount = 0
    for datas in datass:
        # 盈利计算
        for i in range(len(datas)):
            try:datas[i]=float(datas[i])
            except:pass
        # print(datas)
        # print(datas[targetIndex])
        # exit(0)
        # print(type(realValue))
        # print(type(datas[buyPriceindex]))
        # print(type(datas[targetIndex]))
        if datas[statusIndex] == "持有":
            # print("正在计算【{}】【{}】份购买价格【{}】目前价格【{}】目前收益率【{:.2f}%】目标收益率【{:.2f}%】".format(datas[numberIndex],datas[muchIndex],datas[buyPriceindex],realValue,(realValue/datas[buyPriceindex]-1)*100,datas[targetIndex]*100))
            pass

        if datas[statusIndex] == "持有" and realValue > datas[buyPriceindex]*(1+float(datas[targetIndex])):
        # if True:

            msg = "编号为【{编号}】的【{份数}】份基金目前收益率【{当前收益率:.2f}%】超过计划收益率【{目标:.2f}%】可售出".format(
                编号=datas[numberIndex],
                份数=datas[muchIndex],
                当前收益率=(realValue/datas[buyPriceindex]-1)*100,
                目标=datas[targetIndex]*100,
            )
            saleCount=saleCount+datas[muchIndex]
            # print(msg)
            msgList.append(msg)
            continue
    if saleCount != 0:
        msgList.append("合计应出售【{合计出售份数:.2f}】".format(合计出售份数=saleCount))


        # 合并计算
        if datas[statusIndex] == "持有" and realValue < datas[buyPriceindex]*(1-1.5*datas[targetIndex]):
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

def sendMsg(msgList):
    """
    :param msgList:
    :return: 解析消息列表 并发送钉钉消息
    """
    finMsg = ""
    for msg in msgList:
        finMsg=finMsg+msg+"\n"
    发送消息().发送普通文本消息(finMsg, apiurl=robotUrl)

if __name__ == '__main__':

    datass = (GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="hs300"))
    msgList = calculate(datass,HS300REALVALUE)
    sendMsg(msgList)
    # for  i in msgList:
    #     print(i)

    datass = (GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="zz500"))
    msgList = calculate(datass, ZZ500REALVALUE)
    sendMsg(msgList)
    # for  i in msgList:
    #     print(i)













