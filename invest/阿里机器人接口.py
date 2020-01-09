import requests
import json


class 发送消息():
    """官方文档 https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.karFPe&treeId=257&articleId=105735&docType=1 """

    def 发送普通文本消息(self, msg, apiurl, atList=[], isAtAll=False):
        if type(atList) != type([1, 2, 3]):
            return "atList应为列表"
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        str_data = {
            "msgtype": "text",
            "text": {"content": msg + "."},
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

    def 发送MarkDown消息(self, apiurl, title, text, atList=[], isAtAll=False):
        # "text": "#### 杭州天气  \n > 9度， 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/) "
        if type(atList) != type([1, 2, 3]):
            return "atList应为列表"
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        str_data = {
            "msgtype": "markdown",
            "markdown": {"title": title,
                         "text": text,
                         },
            "at": {
                "atMobiles": atList,
                "isAtAll": isAtAll
            }
        }
        json_data = json.dumps(str_data)
        res = requests.post(apiurl, data=json_data, headers=HEADERS)
        return res.text

    def 发送整体跳转消息(self, apiurl, title, localimg="http://cccloud.xyz/static/index.jpeg", singleTitle="singleTitle",
                 singleURL="http://cccloud.xyz/static/index.jpeg"):
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        str_data = {
            "actionCard": {
                "title": title,
                "text": "![]({}) ".format(localimg),
                "hideAvatar": "1",
                "btnOrientation": "0",
                "singleTitle": singleTitle,
                "singleURL": singleURL
            },
            "msgtype": "actionCard"
        }
        json_data = json.dumps(str_data)
        res = requests.post(apiurl, data=json_data, headers=HEADERS)
        return res.text


if __name__ == '__main__':
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=0c57dacf315f6b76a7fa869819820fa108b9eb4111920fb353b2dd22d2d6efd4'
    url = "https://oapi.dingtalk.com/robot/send?access_token=fa20378970ff8f99c854bf4334e1d46e9a33a78bbde78dbfb8f870a85fc876b6"
    # s = 发送消息().发送普通文本消息("测试.", url, isAtAll=True)
    # s = 发送消息().发送链接文本消息(url, "这回对了",
    #                     "详情请点击",
    #                     picUrl="http://img0.imgtn.bdimg.com/it/u=3348813714,2010737230&fm=26&gp=0.jpg",
    #                     messageUrl="http://172.16.241.28:8000/a/"
    #                     )
    # s = 发送消息().发送MarkDown消息(url, "@所有人", "详情请点击")
    s = 发送消息().发送整体跳转消息(url)
    print(s)
