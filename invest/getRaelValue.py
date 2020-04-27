import requests
import json
from tools.transSome import TransSome
import time
import traceback


def getTHHS300A():
    "http://fund.eastmoney.com/110020.html"
    r = requests.get("http://fundgz.1234567.com.cn/js/110020.js?rt={}".format(int(time.time()*1000)))
    res = r.text
    res = res[8:-2]
    res = eval(res)
    return float(res["gsz"])


def getTHZZ500C():
    "http://fund.eastmoney.com/007028.html"
    r = requests.get("http://fundgz.1234567.com.cn/js/007028.js?rt={}".format(int(time.time()*1000)))
    res = r.text
    res = res[8:-2]
    res = eval(res)
    return float(res["gsz"])


def getStock(stockid):
    r = requests.get("http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&id={}1".format(stockid))
    res = eval(r.text.replace("(", "").replace(")", "").replace("false", "False"))
    del res["data"]
    # print(res)
    return res

def getIndex(indexid):

    r = requests.get("http://push2.eastmoney.com/api/qt/stock/details/get?secid=0.399006&fields1=f1,f2,f3,f4&fields2=f51,f52,f53,f54,f55")
    res = eval(r.text.replace("(", "").replace(")", "").replace("false", "False"))
    return res["data"]


def getNewStock(stocktype="bond", num=50):
    """
    http://data.eastmoney.com/kzz/default.html
    :parma:stocktype bond ipo
    :return: 获取可转债状态列表
    """
    try:
        # stockdic = {"bond": "KZZ_LB2.0", "ipo": "XGSG_LB"}
        if stocktype == "ipo":
            url = "http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=XGSG_LB&token=70f12f2f4f091e459a279469fe49eca5&st=purchasedate,securitycode&sr=-1&p=1&ps={num}".format(num=num)
        if stocktype == "bond":
            url =  "http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=KZZ_LB2.0&token=70f12f2f4f091e459a279469fe49eca5&st=STARTDATE&sr=-1&p=-1&ps={num}".format(num=num)
        r = requests.get(url)

        return json.loads(r.text)
    except:
        return "怀疑接口token已经变更"


def getNewStockZQH(code):
    """http://data.eastmoney.com/xg/xg/detail/603236.html"""
    try:
        r = requests.get(
                "http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=XGSG_ZQH&token=70f12f2f4f091e459a279469fe49eca5&st=LASTFIGURETYPE&sr=1&filter=(securitycode='{}')".format(
                    code))
        dic = json.loads(r.text)
        res = {}
        for i in dic:
            res[i["LASTFIGURETYPE"]] = i["LOTNUM"].split(",")
        res = TransSome().dicListStr2Int(res)
        return res
    except:
        return "怀疑接口token已经变更"

def getNewBondZQH(code):
    """http://data.eastmoney.com/kzz/detail/113540.html"""
    try:
        r = requests.get(
                "http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=KZZ_ZQH&token=70f12f2f4f091e459a279469fe49eca5&st=LASTFIGURETYPE&sr=1&filter=(BONDCODE='{}')".format(code)
            )
        # print(r.text)
        dic = json.loads(r.text)
        if dic[0]["LUCKNUM"] =="":
            return {}
        res = {}
        for i in dic:
            res[i["TYPECODE"]] = i["LUCKNUM"].split(",")
        res = TransSome().dicListStr2Int(res)
        return res
    except:
        return "怀疑接口token已经变更"

if __name__ == '__main__':
    # print(getNewStockZQH("603256"))
    # print(getNewBondZQH("123036"))
    hs300=getTHHS300A()
    zz500=getTHZZ500C()
    print(hs300)
    print(zz500)
    # s = getStock(stockid = "399006")
    # s = getNewStock("bond")
    # s = getNewStock("ipo")
    # s= getIndex("399006")
    # print(s)
    # print(s["info"]["c"])
    1.3425
    1.0599

