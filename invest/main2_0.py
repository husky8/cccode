# coding=utf-8
import sys
import os
import time

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
    编号index = keys.index('编号')
    成本index = keys.index('成本')
    份数index = keys.index('份数')
    购单价index = keys.index('购单价')
    目标index = keys.index('目标')
    售单价index = keys.index('售单价')
    盈利index = keys.index('盈利')
    状态index = keys.index('状态')
    日志index = keys.index('日志')

    msgList=[]

    for datas in datass:
        # 盈利计算
        for i in range(len(datas)):
            try:datas[i]=float(datas[i])
            except:pass
        # print(datas)
        # print(datas[目标index])
        # exit(0)
        # print(type(realValue))
        # print(type(datas[购单价index]))
        # print(type(datas[目标index]))

        if datas[状态index] == "持有" and realValue > datas[购单价index]*(1+float(datas[目标index])):
        # if True:

            msg = "编号为【{编号}】的【{份数}】份基金目前收益率【{当前收益率:.2f}%】超过计划收益率【{目标:.2f}%】可售出".format(
                编号=datas[编号index],
                份数=datas[份数index],
                当前收益率=(realValue/datas[购单价index]-1)*100,
                目标=datas[目标index]*100,
            )
            # print(msg)
            msgList.append(msg)
            continue

        # 合并计算
        if datas[状态index] == "持有" and realValue < datas[购单价index]*(1-1.5*datas[目标index]):
        # if True:
            msg = "编号为【{编号}】的【{份数}】份基金目前收益率【{当前收益率:.2f}%】请考虑合并".format(
                编号=datas[编号index],
                份数=datas[份数index],
                当前收益率=(realValue / datas[购单价index] - 1) * 100,
                目标=datas[目标index] * 100,
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
    # print(msgList)
    sendMsg(msgList)

    datass = (GetInfoFromExcel().getInfoFromExcel(configFilePath, sheetName="zz500"))
    msgList = calculate(datass, ZZ500REALVALUE)
    sendMsg(msgList)
    # print(msgList)














