import sys
import os
sys.path.append("..")
sys.path.append(os.getcwd())
from invest.EXCEL封装 import GetInfoFromExcel
from invest.EXCEL封装 import WriteDataToExcel
from invest.EXCEL封装 import CreateNewWorkbook
from invest.getRaelValue import getTHHS300A
from invest.getRaelValue import getTHZZ500C
from invest.阿里机器人接口 import 发送消息

HS300REALVALUE=getTHHS300A()
ZZ500REALVALUE=getTHZZ500C()
print(HS300REALVALUE)
print(ZZ500REALVALUE)
robotUrl = "https://oapi.dingtalk.com/robot/send?access_token=c1c7e7ee961fd1049876fe87d98cdbf6ba106cfa3a5f616333e33cbfc780db98"

datass=(GetInfoFromExcel().getInfoFromExcel("配置.xlsx",sheetName="hs300"))
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
        # if datas[状态index] == "持有" and realValue > datas[购单价index]*(1+datas[目标index]):
        if True:

            msg = "编号为【{编号}】的【{份数}】份基金目前收益率【{当前收益率:.2f}%】超过计划收益率【{目标}%】可售出".format(
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

    datass = (GetInfoFromExcel().getInfoFromExcel("配置.xlsx", sheetName="hs300"))
    msgList = calculate(datass,HS300REALVALUE)
    sendMsg(msgList)

    datass = (GetInfoFromExcel().getInfoFromExcel("配置.xlsx", sheetName="zz500"))
    msgList = calculate(datass, ZZ500REALVALUE)
    sendMsg(msgList)

# CreateNewWorkbook().createNewWorkbook("结果.xlsx",["发帖人名称","推送次数","总发文量",
#             "总阅读量","总点赞数","头条总阅读量","头条总点赞数","头条最高阅读","头条最高点赞"]) #写首行
# WriteDataToExcel().writeDataToExcel("结果.xlsx",finResult) #写正文














