def changeJson(targetJson,jsonRE,replaceOnly=True):
    """
    :param targetJson:需要进行操作的json
    :param jsonRE: {k:v,}K需要操作的节点 |||分割层级
    :param replaceOnly:默认True 即只替换源节点 不生成新节点
    :return:处理后的json
    """
    replaceOnly=False
    jsonRE={"record|||queryStrings|||0|||id":"222","environment":"333","sss":"www"}
    targetJson={"environment":"kkkkk","record":{"queryStrings":[{"id":"a5012310-d5a7-11e8-8b66-d9ef04ae19b8-ryOWk6qom","key":"channel_id","value":"1","sort":0,"isActive":True}],"headers":[{"id":"df267600-d5a5-11e8-8b66-d9ef04ae19b8-S1lCZ3h9oQ","key":"Cookie","value":"sess=M2MzY2N8MTU0NTExNzAyM3wxODExNjEwNzc2fGJhMWJlM2ViMWQ1MThkNGQxNjljNjA1ZGE0NmI3NThm;","isActive":True,"isFav":False,"sort":0,"description":None},{"id":"df267601-d5a5-11e8-8b66-d9ef04ae19b8-HyWAb23qim","key":"Host","value":"haojia-api.smzdm.com","isActive":True,"isFav":False,"sort":1,"description":None}],"formDatas":[],"children":[],"id":"df264ef0-d5a5-11e8-8b66-d9ef04ae19b8-HJC-nn9om","assertInfos":{"root/error_msg":[],"root/error_code":[]},"category":20,"name":"获取好价详情页","url":"http://{{env}}:809/v1/articles/9509124","method":"GET","body":"","bodyType":None,"parameters":None,"reduceAlgorithm":0,"parameterType":0,"dataMode":1,"prescript":"","test":"","sort":380164,"version":None,"description":None,"createDate":"2018-09-11T07:15:23.530Z","updateDate":"2018-09-11T11:02:30.011Z","collection":{"id":"6bad43d0-b592-11e8-8328-6fbcb798990a-rywYokHO7","name":"9.0发现","commonPreScript":"","reqStrictSSL":False,"reqFollowRedirect":False,"description":"","recycle":False,"public":True,"commonSetting":{"test":"","headers":[],"prescript":""},"createDate":"2018-09-11T07:15:11.118Z","updateDate":"2018-09-11T07:15:11.118Z"},"history":[],"collectionId":"952f69c0-d5a6-11e8-8b66-d9ef04ae19b8-SJgBa29om","pid":""}}

    if type(jsonRE) !=type({"a":"b"}):
        print("替换规则传参错误,未修改json")
        return targetJson
    for k,v in jsonRE.items():
        k_items=k.split("|||")
        len_k_items=len(k_items)
        for i in range(len_k_items):
            try:
                k_items[i]=int(k_items[i])
            except:
                pass
        # print(k)
        if len_k_items == 1:
            if replaceOnly :
                try:
                    temp = targetJson[k_items[0]]
                except :
                    print("给定的键{k}不存在，当前设定为仅替换，故未新增{k}键".format(k=k))
                    continue
            targetJson[k_items[0]] = v

        if len_k_items == 2:
            if replaceOnly :
                try:
                    temp = targetJson[k_items[0]][k_items[1]]
                except :
                    print("给定的键{k}不存在，当前设定为仅替换，故未新增{k}键".format(k=k))
                    continue
            targetJson[k_items[0]][k_items[1]] = v

        if len_k_items == 3:
            if replaceOnly:
                try:
                    temp = targetJson[k_items[0]][k_items[1]][k_items[2]]
                except :
                    print("给定的键{k}不存在，当前设定为仅替换，故未新增{k}键".format(k=k))
                    continue
            targetJson[k_items[0]][k_items[1]][k_items[2]] = v

        if len_k_items == 4:
            if replaceOnly:
                try:
                    temp = targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]]
                except :
                    print("给定的键{k}不存在，当前设定为仅替换，故未新增{k}键".format(k=k))
                    continue
            targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]] = v

        if len_k_items == 5:
            if replaceOnly:
                try:
                    temp = targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]][k_items[4]]
                except :
                    print("给定的键{k}不存在，当前设定为仅替换，故未新增{k}键".format(k=k))
                    continue
            targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]][k_items[4]] = v

        if len_k_items == 6:
            if replaceOnly:
                try:
                    temp = targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]][k_items[4]][k_items[5]]
                except :
                    print("给定的键{k}不存在，当前设定为仅替换，故未新增{k}键".format(k=k))
                    continue
            targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]][k_items[4]][k_items[5]] = v

        if len_k_items == 7:
            if replaceOnly:
                try:
                    temp = targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]][k_items[4]][k_items[5]][k_items[6]]
                except :
                    print("给定的键{k}不存在，当前设定为仅替换，故未新增{k}键".format(k=k))
                    continue
            targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]][k_items[4]][k_items[5]][k_items[6]] = v

        if len_k_items == 8:
            if replaceOnly:
                try:
                    temp = targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]][k_items[4]][k_items[5]][k_items[6]][k_items[7]]
                except :
                    print("给定的键{k}不存在，当前设定为仅替换，故未新增{k}键".format(k=k))
                    continue
            targetJson[k_items[0]][k_items[1]][k_items[2]][k_items[3]][k_items[4]][k_items[5]][k_items[6]][k_items[7]]= v

        if len_k_items > 8:
            print("层级太多了，增加下底层脚本吧")

    return targetJson




