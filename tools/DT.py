import traceback
from tools import config
import sxtwl
import os
import re
import math
import datetime
import requests
import json





def getWorkDayDiff(startDate = "",diff = -1):
    """
    :param startDate:
    :param diff:
    :return:
    """
    if startDate == "":
        startDate = datetime.date.today()
    else:
        startDate.replace("-", "").replace("_", "").replace("/", "").replace("-", "")
        startDate = datetime.datetime(int(startDate[0:4]), int(startDate[4:6]), int(startDate[6:8]))
    for i in range(1, math.ceil(1.4*abs(diff)+10)):
        s_day = get_day_property(str(startDate - datetime.timedelta(days=i if diff<0 else -i)))
        if s_day["data"]["workday"]:
            diff = diff+1 if diff<0 else diff-1
            if diff==0:
                return s_day["data"]["Solar"]

def getMarketDayDiff(startDate = "",diff = -1):
    """
    :param startDate:
    :param diff:
    :return:
    """

    if startDate =="":
        startDate = datetime.date.today()
    else:
        startDate = startDate.replace("-", "").replace("_", "").replace("/", "").replace("-", "")
        print(startDate)
        startDate = datetime.datetime(int(startDate[0:4]),int(startDate[4:6]),int(startDate[6:8]))
    for i in range(1, math.ceil(1.4*abs(diff)+10)):
        s_day = get_day_property(str(startDate - datetime.timedelta(days=i if diff<0 else -i)))
        if s_day["data"]["workday"] is True and 0<= s_day["data"]["weekday"] <=5:
            diff = diff+1 if diff<0 else diff-1
            if diff==0:
                return s_day["data"]["Solar"][:8]

def get_day_property(date=""):
    """
    获取日期的属性
    :param date: 支持 YYYYMMDD YYYY.MM.DD YYYY/MM/DD YYYY-MM-DD YYYY_MM_DD
    :return: DayProperty
    """
    try:
        if date == "":
            date = str(datetime.date.today())
        date = date.replace("-", "").replace("_", "").replace("/", "").replace("-", "")
        y = int(date[0:4])
        m = int(date[4:6])
        d = int(date[6:8])
        lunar = sxtwl.Lunar()  # 实例化日历库d
        day = lunar.getDayBySolar(y, m, d)
        if day.Lleap:
            r_lunar = "闰{}月{}".format(config.YMC[day.Lmc], config.RMC[day.Ldi])
        else:
            r_lunar = "闰{}月{}".format(config.YMC[day.Lmc], config.RMC[day.Ldi])
        weekday = datetime.datetime(y, m, d).weekday()
        if date in config.WORK_DAY:
            return {"error_code": "", "error_msg": "", "data": {"Solar": date, "weekday":weekday+1,"workday": True, "lunar": r_lunar}}
        if date in config.FREE_DAY:
            return {"error_code": "", "error_msg": "", "data": {"Solar": date, "weekday":weekday+1,"workday": False, "lunar": r_lunar}}

        if 0 <= weekday <= 4:
            return {"error_code": "", "error_msg": "", "data": {"Solar": date, "weekday":weekday+1,"workday": True, "lunar": r_lunar}}
        else:
            return {"error_code": "", "error_msg": "", "data": {"Solar": date, "weekday":weekday+1,"workday": False, "lunar": r_lunar}}
    except ValueError:
        return {"error_code": "1", "error_msg": traceback.format_exc().split("\n")[-2], "data": ""}


def get_git_history():
    os.system(" git -c diff.mnemonicprefix=false -c core.quotepath=false pull origin dev ")
    os.system(
        "git log --after='{b30day} 00:00:00' --graph --date=format:'%Y-%m-%d %H:%M:%S' "
        "--pretty=format:'%Cred%h%Creset - 【%an】 %C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)%Creset' "
        "> 1111.txt".format(b30day=datetime.date.today() - datetime.timedelta(days=30))
    )
    f = open("log.txt", encoding="utf-8")
    res = {}
    for line in f.readlines():
        try:
            re_name = re.compile(r'[【](.*?)[】]', re.S)
            re_name_l = (re.findall(re_name, line))
            name = re_name_l[-1]
            re_date = re.compile(r'[(](.*?)[)]', re.S)
            re_date_l = (re.findall(re_date, line))
            date = re_date_l[-1]
            if len(re_date_l) == 1:
                re_desc = re.compile(r'[】](.*?)[(]', re.S)
            else:
                re_desc = re.compile(r'[)](.*?)[(]', re.S)
            re_desc_l = (re.findall(re_desc, line))
            desc = re_desc_l[0]
        except IndexError:
            continue
        try:
            res[name].append({"date": date, "desc": desc})
        except KeyError:
            res[name] = []
            res[name].append({"date": date, "desc": desc})
    return res


if __name__ == '__main__':
    # logger.info(get_day_property())
    # get_git_history()
    # logger.info(get_stream("6112012771547294013460069da3589848fc84d5f2f1aa6c49284b25"))
    # print(getMarketDayDiff("20190617",diff = -5))
    a = getMarketDayDiff("2021-01-26",-2)
    print(a)
    pass
