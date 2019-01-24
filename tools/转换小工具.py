
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

print(cookiekv2dicKV("loginStatus=user; JSESSIONID=BAB924D0DEB51294F8AB381480B3C5F9;__ckguid=H8X6gu7uJUAWk96KAQRClv; ZDM_CAS_SESS_ID=ST-2842-1NG-5to-HRsOpPZY0XNFBbu8IU4-asso-230; device_id=352400463015422524242098184f59cd5688c9105d826dfaabe6bedbf1; _ga=GA1.2.269687424.1542252427; smzdm_user_source=BB2AEAB95FFB986BF902966EBDB5E3B5; wt3_eid=%3B999768690672041%7C2154226826100310557%232154414958300253266; PHPSESSID=41a704b90812f3ca2c17088746687a4b; pac4jCsrfToken=1178ac17-8003-4c29-9d9f-ce61e7231d91; wt3_sid=%3B999768690672041; smzdm_user_view=DD2DDD0E66935458732EEF82B5EF5801; ss_ab=ss81; zdm_qd=%7B%7D; _gid=GA1.2.1343850324.1544672626; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%229c3fd7ec24249427b785a4940535a54e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%2210.10.160.126%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A82%3A%22Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10.13%3B+rv%3A63.0%29+Gecko%2F20100101+Firefox%2F63.0%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1544694229%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D59c733045ceca539bc66ec017bf0cd7c"))
