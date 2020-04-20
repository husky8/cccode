import urllib.parse
def urlkv2dicKV(urlKV):

    """
    :param urlKV: like  v=9.1.0.12&weixin:0
    :return: dicKV like {"v":"9.1.0.12","weixin"="0"}
    """

    kvlist=urlKV.split("&")
    print(kvlist)
    dic={}
    for i in kvlist:
        print(i)
        dic[i.split("=")[0]]= i.split("=")[1]
    return dic

def cookiekv2dicKV(urlKV):

    """
    :param urlKV: like  v=9.1.0.12&weixin:0
    :return: dicKV like {"v":"9.1.0.12","weixin"="0"}
    """

    kvlist=urlKV.split(";")
    print(kvlist)
    dic={}
    for i in kvlist:
        print(i)
        dic[i.split("=")[0]]= i.split("=")[1]
    return dic

def dicKV2URLkv(dicKV):
    """
    :param dicKV: like {"v":"9.1.0.12","weixin":"0"}
    :return: urlKV like  v=9.1.0.12&weixin=0
    """
    res=""
    for k,v in dicKV.items():
        res=res+k+"="+v+"&"
    return res[:-1]
def urldecode(s):
    return urllib.parse.unquote(s)

# print(cookiekv2dicKV("loginStatus=user; JSESSIONID=BAB924D0DEB51294F8AB381480B3C5F9;__ckguid=H8X6gu7uJUAWk96KAQRClv; ZDM_CAS_SESS_ID=ST-2842-1NG-5to-HRsOpPZY0XNFBbu8IU4-asso-230; device_id=352400463015422524242098184f59cd5688c9105d826dfaabe6bedbf1; _ga=GA1.2.269687424.1542252427; smzdm_user_source=BB2AEAB95FFB986BF902966EBDB5E3B5; wt3_eid=%3B999768690672041%7C2154226826100310557%232154414958300253266; PHPSESSID=41a704b90812f3ca2c17088746687a4b; pac4jCsrfToken=1178ac17-8003-4c29-9d9f-ce61e7231d91; wt3_sid=%3B999768690672041; smzdm_user_view=DD2DDD0E66935458732EEF82B5EF5801; ss_ab=ss81; zdm_qd=%7B%7D; _gid=GA1.2.1343850324.1544672626; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%229c3fd7ec24249427b785a4940535a54e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%2210.10.160.126%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A82%3A%22Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10.13%3B+rv%3A63.0%29+Gecko%2F20100101+Firefox%2F63.0%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1544694229%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D59c733045ceca539bc66ec017bf0cd7c"))
# print(urlkv2dicKV("pid=10803&issuetype=10602&atl_token=BNV7-M0ZA-E8SS-R4OK_f55500c5ef91a8f9cbf1cde47edda0a94048bc55_lin&formToken=b0ef56026f45fea14c128b8a7e501ee321dcd5ec&summary=%E9%99%88%E7%A8%8B-20190325+%E6%8E%A8%E8%8D%90931%E7%94%A8%E4%BE%8B%E7%BC%96%E5%86%99&customfield_10308=10403&customfield_10308%3A1=&description=&customfield_10422=2019-03-25&timetracking_originalestimate=8.6&timetracking_remainingestimate=8.6&isCreateIssue=true&hasWorkStarted=&fieldsToRetain=project&fieldsToRetain=issuetype&fieldsToRetain=customfield_10308&fieldsToRetain=customfield_10422"))
# print(urlkv2dicKV("https://www.google-analytics.com/collect?v=1&_v=j73&a=662429186&t=event&ni=0&_s=1&dl=https%3A%2F%2Fwww.smzdm.com%2Fbaoliao%2F&ul=zh-cn&de=UTF-8&dt=%E6%88%91%E8%A6%81%E7%88%86%E6%96%99%20%7C%20%E7%BD%91%E5%8F%8B%E4%BC%98%E6%83%A0%E4%BF%83%E9%94%80%E4%BF%A1%E6%81%AF%E6%8F%90%E4%BA%A4%E9%A1%B5%E9%9D%A2_%E4%BB%80%E4%B9%88%E5%80%BC%E5%BE%97%E4%B9%B0&sd=24-bit&sr=1920x1080&vp=1321x1001&je=0&ec=PC%E7%88%86%E6%96%99%E6%8A%95%E7%A8%BF&ea=%E8%8E%B7%E5%8F%96%E4%BF%A1%E6%81%AF&el=%E5%8D%95%E5%93%81%E7%88%86%E6%96%99&_u=SCCAAAAL~&jid=&gjid=&cid=1102403403.1552983705&uid=8910558812&tid=UA-27058866-1&_gid=1280491777.1553839516&gtm=2wg3i1P6RFTX&cd8=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_14_2)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F72.0.3626.121%20Safari%2F537.36&cd16=8910558812&cd26=%E6%B2%A1%E6%9C%89%E5%B1%8F%E8%94%BD&cd80=1102403403.1552983705&cd103=a&z=859056686"))