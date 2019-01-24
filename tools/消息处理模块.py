from tools.阿里机器人接口 import 发送消息
import getpass #用于区分是不是正式环境的

class 发送钉钉消息():
    if getpass.getuser() != 'zhxg':
        hearturl = ''
        warnningurl=""
    else:
        hearturl=''
        warnningurl=''

    def 发送钉钉普通消息(self,正文,level="心跳",atList=[],atAll=False):
        if level=="心跳":url=self.hearturl
        if level=="报警":url=self.warnningurl
        sendLog = 发送消息().发送普通文本消息(正文,url,atList,atAll)
        if sendLog =='{"errcode":0,"errmsg":"ok"}':
            return True

if __name__ == '__main__':
    发送钉钉消息().发送钉钉普通消息("111111")