import requests
import time

curtime = int(time.time()*1000)

print("http://www.114yygh.com/web/getVerifyCode?mobile=18888851041&smsKey=ORDER_CODE&rd={}".format(curtime))
# r = requests.get("http://www.114yygh.com/web/getVerifyCode?mobile=18888851041&smsKey=ORDER_CODE&rd={}".format(curtime))
# print(r.text)