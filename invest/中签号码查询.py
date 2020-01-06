from tools.colorLog import colorLog
from invest.getRaelValue import getNewStockZQH, getNewBondZQH
import time


# code = input("请输入股票/债权代码:")
# start = int(input("请输入起始配号:"))
# num = int(input("输入配号数量:"))


def getBoundsRes(code, start, num, title="客官", name=""):
    if code[0] in ["0", "3", "6"]:
        中签矩阵 = getNewStockZQH(code)
    else:
        中签矩阵 = getNewBondZQH(code)

    if 中签矩阵 == {}:
        colorLog("---------FBI  WARNING---------\n{} 骚等【{}】尚未发布中签号码\n".format(title, code if name == "" else name),
                 fontColor="黄")
        return 0
    if 中签矩阵 == "怀疑接口token已经变更":
        colorLog("---------FBI  WARNING---------\n{} 骚等【{}】查询失败 \n".format(title, code if name == "" else name),
                 fontColor="紫")
        return 0

    # 中签矩阵 = {"4": [94, 2094, 4094, 6094, 8094, 5359],"5": [44823, 94823, 70555], "6": [677381, 802381, 927381, 552381, 427381, 302381, 177381, 52381],"7": [5897867, 7147867, 8397867, 9647867, 4647867, 3397867, 2147867, 897867, 6888056],"9": [304456913, 156096611, 31287275],}
    # print(中签矩阵)
    s = time.time()
    res = []
    # try:
    #     for i in 中签矩阵.keys():
    #         for j in 中签矩阵[i]:
    #             if start % 10 ** int(i) <= j <= (start + num) % 10 ** int(i):
    #                 res.append("{}{}".format(str(start)[:-len(str(j))], j))

    try:
        for i in range(start, start + num):

            for j in 中签矩阵.keys():
                # print(j)
                for k in 中签矩阵[j]:
                    # print(i%(10^int(j)))
                    if i % (10 ** int(j)) == k:
                        res.append(i)
    except AttributeError:
        pass

    if res == []:
        colorLog(" --- 很  遗  憾 --- \n{} 【{}】您未中签\n".format(title, code if name == "" else name), fontColor="蓝")
    else:
        colorLog("--- 恭 喜 {} --- \n【{}】喜中【{}】签\n--- 中 签 号 码 ---".format(" ".join(title), code if name == "" else name,
                                                                        len(res)), fontColor="红")
        for i in res:
            colorLog(str(i), fontColor="红")
    print("\n")


if __name__ == '__main__':
    getBoundsRes("127015", 756295120, 1000, "帅程", "希望转债")
    getBoundsRes("128093", 733150530, 1000, "帅程", "百川转债")
    getBoundsRes("123040", 486527427, 1000, "帅程", "乐普转债")
    # getBoundsRes("113561", 100819957996, 1000, "帅程", "正裕转债")
    # getBoundsRes("128090", 625757509, 1000, "帅程", "汽模转2")
    # getBoundsRes("123038", 793537887, 1000, "帅程", "联得转债")
    # getBoundsRes("128088", 827445181, 1000, "帅程", "深南转债")
    # getBoundsRes("113030", 100816404486, 1000, "帅程", "东风转债")
    # getBoundsRes("113559", 100805025479, 1000, "哈哥", "永创转债")
    # getBoundsRes("113558", 100801177589, 1000, "哈哥", "日月转债")
    # getBoundsRes("110065", 100773099954, 1000, "哈哥", "淮矿转债")
    # getBoundsRes("113559", 101007379754, 1000, "帅程", "永创转债")
    # getBoundsRes("113558", 101044695212, 1000, "帅程", "日月转债")
    # getBoundsRes("110065", 101045099683, 1000, "帅程", "淮矿转债")
    # getBoundsRes("110064", 100710510305, 1000, "帅程", "建工转债")
    # getBoundsRes("113556", 100653685108, 1000, "帅程", "至纯转债")
    # getBoundsRes("128086", 699613430, 1000, "哈哥", "国轩转债")
    # getBoundsRes("128087", 662010056, 1000, "哈哥", "孚日转债")
    # getBoundsRes("128086", 643558840, 1000, "帅程", "国轩转债")
    # getBoundsRes("128087", 607062245, 1000, "帅程", "孚日转债")
    # getBoundsRes("113029", 100560433412, 1000, "哈哥", "明阳转债")
    # getBoundsRes("128084", 562517466, 1000, "哈哥", "木森转债")
    # getBoundsRes("113554", 100533268582, 1000, "哈哥", "仙鹤转债")
    # getBoundsRes("128085", 549790621, 1000, "哈哥", "鸿达转债")
    # getBoundsRes("113029", 100630879121, 1000, "帅程","明阳转债")
    # getBoundsRes("128084", 625649904, 1000, "帅程","木森转债")
    # getBoundsRes("113554", 100629199191, 1000, "帅程","仙鹤转债")
    # getBoundsRes("128085", 625699348, 1000, "帅程","鸿达转债")
    # getBoundsRes("113553", 100327618527, 1000, title="哈哥",name = "金牌转债")  # 金牌转债
    # getBoundsRes("110063", 100332516415, 1000, title="哈哥",name = "鹰19转债")  # 鹰19转债
    # getBoundsRes("113553", 101055199378, 1000, "帅程")  # 金牌转债
    # getBoundsRes("110063", 101062728501, 1000, "帅程")  # 鹰19转债
    # getBoundsRes("123036", 398485156, 1000, "帅程")  # 先导转债
    # getBoundsRes("601512", 100015187482, 11, "帅程")  # 中新集团
    # getBoundsRes("603995", 100011564613, 11, "帅程")  # 甬金股份
    # getBoundsRes("110062", 100303220820, 1000, "哈哥")  # 烽火转债
    # getBoundsRes("110062", 100522780454, 1000, "帅程")  # 顺丰转债
    # getBoundsRes("128080", 846510200, 1000, "帅程")  # 顺丰转债
    # getBoundsRes("113551", 100819534460, 1000, "帅程")  # 福特转债
    # getBoundsRes("113550", 100785452348, 1000, "帅程")  # 常汽转债
    # getBoundsRes("128080", 841962586, 1000, "哈哥")  # 顺丰转债
    # getBoundsRes("113551", 100813990142, 1000, "哈哥")  # 福特转债
    # getBoundsRes("123034", 397688611, 1000, "帅程")  # 通光转债
    # getBoundsRes("110060", 100382940471, 1000, "哈哥")  # 天路转债
    # getBoundsRes("113548", 100381580532, 1000, "哈哥")  # 石英转债
    # getBoundsRes("110059", 100389754825, 1000, "哈哥")  # 浦发转债
    # getBoundsRes("110060", 100386667008, 1000, "帅程")  # 天路转债
    # getBoundsRes("113548", 100385177301, 1000, "帅程")  # 石英转债
    # getBoundsRes("110059", 100393559790, 1000, "帅程")  # 浦发转债
    # getBoundsRes("113547", 100366876902, 1000, "帅程")  # 索发转债
    # getBoundsRes("127014", 388510743, 1000, "帅程")  # 北方转债
    # getBoundsRes("113546", 100617481620, 1000, "帅程")  # 迪贝转债
    # getBoundsRes("128078", 605115596, 1000, "哈哥")  # 太极转债
    # getBoundsRes("128079", 562227584, 1000, "帅程") #英联转债
    # getBoundsRes("128078", 605077385, 1000, "帅程") #太极转债
    # getBoundsRes("128077", 657240490, 1000, "哈哥")
    # getBoundsRes("128077", 347609197, 1000, "帅程")
    # getBoundsRes("128076", 301265397, 1000,"哈哥")
    # getBoundsRes("113545", 100294212867, 1000,"哈哥")
    # getBoundsRes("601077", 100042420002, 1,"哈哥")
    # getBoundsRes("128076", 671952030, 1000,"帅程")
    # getBoundsRes("113545", 100645082309, 1000,"帅程")
    # getBoundsRes("601077", 100220187951, 8,"帅程")
    # getBoundsRes("603786", 100017731131, 8,"帅程")
    # getBoundsRes("603786", 100023976995, 1,"哈哥")
    # getBoundsRes("128075", 600663402, 1000)
    # getBoundsRes("113544", 1000807778521, 1000)
    # getBoundsRes("123030", 160442843, 1000)
    # getBoundsRes("603115", 100003200381, 6)
    # getBoundsRes("603530", 100005686774, 5)
    # getBoundsRes("113541", 100170380811, 1000)
    # getBoundsRes("002966", 100009633317, 4)
    # getBoundsRes("603613", 100009633317, 4)
    # getBoundsRes("002957", 1000016462683, 2)
    # getBoundsRes("603279", 1000011658073, 4)
    # getBoundsRes("603983", 100007855706, 4)
    # getBoundsRes("603687", 100008977755, 4)
