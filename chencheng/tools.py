import datetime
import traceback
import chencheng.config as config
import sxtwl
def getDayProperty(date=""):
    """
    获取日期的属性
    :param date: 支持 YYYYMMDD YYYY.MM.DD YYYY/MM/DD YYYY-MM-DD YYYY_MM_DD
    :return: DayProperty
    """
    try:
        if date == "" :date = str(datetime.date.today())
        date = date.replace("-","").replace("_","").replace("/","").replace("-","")
        y = int(date[0:4])
        m = int(date[4:6].replace("0",""))
        d = int(date[6:8].replace("0",""))
        lunar = sxtwl.Lunar()  # 实例化日历库d
        day = lunar.getDayBySolar(y , m , d )
        if day.Lleap:
            rlunar = "润{}月{}".format(config.YMC[day.Lmc], config.RMC[day.Ldi])
        else:
            rlunar = "{}月{}".format(config.YMC[day.Lmc],  config.RMC[day.Ldi])

        if date in config.WORKDAY:
            return {"error_code": "", "error_msg": "", "data": {"Solar":date,"workday":True,"lunar":rlunar}}
        if date in config.FREEDAY:
            return {"error_code": "", "error_msg": "", "data": {"Solar":date,"workday":False,"lunar":rlunar}}
        if 1 <= datetime.datetime(y,m,d).weekday() <=5:
            return {"error_code": "", "error_msg": "", "data": {"Solar":date,"workday":True,"lunar":rlunar}}
        else:
            return {"error_code": "", "error_msg": "", "data": {"Solar":date,"workday":False,"lunar":rlunar}}
    except:
        return  {"error_code": "1", "error_msg": traceback.format_exc().split("\n")[-2], "data": ""}
if __name__ == '__main__':
    print(getDayProperty())
    pass
