import requests
import json


class 发送消息():
    """官方文档 https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.karFPe&treeId=257&articleId=105735&docType=1 """

    def 发送普通文本消息(self, msg, apiurl,  atList=[], isAtAll=False):
        if type(atList) != type([1, 2, 3]):
            return "atList应为列表"
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        str_data = {
            "msgtype": "text",
            "text": {"content": msg},
            "at": {
                "atMobiles": atList,
                "isAtAll": isAtAll
            }
        }
        json_data = json.dumps(str_data)
        res = requests.post(apiurl, data=json_data, headers=HEADERS)
        return res.text

    def 发送链接文本消息(self, apiurl, title, text="", picUrl="", messageUrl="http://www.baidu.com"):
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        str_data = {
            "msgtype": "link",
            "link": {
                "title": title,
                "text": text,
                "picUrl": picUrl,
                "messageUrl": messageUrl
            }
        }
        json_data = json.dumps(str_data)
        res = requests.post(apiurl, data=json_data, headers=HEADERS)
        return res.text

    def 发送MarkDown消息(self, apiurl, title, text, atList=[],isAtAll=False):
        # "text": "#### 杭州天气  \n > 9度， 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/) "
        if type(atList) != type([1, 2, 3]):
            return "atList应为列表"
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        str_data = {
            "msgtype": "markdown",
            "markdown": {"title": title,
                         "text":text,
                         },
            "at": {
                "atMobiles": atList,
                "isAtAll": isAtAll
            }
        }
        json_data = json.dumps(str_data)
        res = requests.post(apiurl, data=json_data, headers=HEADERS)
        return res.text


if __name__ == '__main__':
    url = "https://oapi.dingtalk.com/robot/send?access_token=cf51a41dccf6b742196dae89e6b73c586c89761d50695d29fb2712c314eb9b13"
    发送消息().发送普通文本消息("乐乐接旨，午门外剁了",url)
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=0c57dacf315f6b76a7fa869819820fa108b9eb4111920fb353b2dd22d2d6efd4'
    # url="https://oapi.dingtalk.com/robot/send?access_token=5985b0b1d4f41624575d46c350fd8413d5ce32106889446fef74735e06e75b4b"
    # 发送消息().发送普通文本消息("小伙伴们，本周六(12.29)中午呷哺呷哺，约的吱一声",url,isAtAll=True)
    # s = 发送消息().发送链接文本消息(url, "这回对了",
    #                     "详情请点击",
    #                     picUrl="http://img0.imgtn.bdimg.com/it/u=3348813714,2010737230&fm=26&gp=0.jpg",
    #                     messageUrl="http://172.16.241.28:8000/a/"
    #                     )
    # s = 发送消息().发送MarkDown消息(url, "@所有人", "详情请点击")
    # print(s)

