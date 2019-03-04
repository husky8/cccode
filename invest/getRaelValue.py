import requests
import json

def getTHHS300A():
    "http://fund.eastmoney.com/000961.html"
    r=requests.get("http://fundgz.1234567.com.cn/js/000961.js?rt=1547013082197")
    res=r.text
    res=res[8:-2]
    res=eval(res)
    return float(res["gsz"])

def getTHZZ500C():
    "http://fund.eastmoney.com/005919.html"
    r = requests.get("http://fundgz.1234567.com.cn/js/005919.js?rt=1547013082197")
    res = r.text
    # print(res)
    res = res[8:-2]
    res = eval(res)
    return float(res["gsz"])

if __name__ == '__main__':
    hs300=getTHHS300A()
    zz500=getTHZZ500C()
    print("hs300 {}".format(hs300))
    print("zz500 {}".format(zz500))
