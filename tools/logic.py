def isColor(color):
    """判断给定参数书否满足（r，g，b）要求"""
    if type(color) != type((1,2,3)) or len(color) != 3:
        print("请输入（R,G,B) 数组，其中RGB应为0~255的整数")
        return False
    for i in color:
        if type(i) != type(1) or i<0 or i>255:
            print("请输入（R,G,B) 数组,其中RGB应为 0~255的整数")
            return False
    return True

def isRect(rect):
    """判断给定参数书否满足（a，b）且为矩形要求"""
    if type(rect) != type((1,2)) or len(rect) != 2:
        print("请输入（A,B) 数组，其中AB应为正整数")
        return False
    for i in rect:
        if type(i) != type(1) or i<= 0 :
            print("请请输入（A,B) 数组，其中AB应为正整数")
            return False
    return True