def bubbleSort(tlist):
    """
    复杂度 O^2
    第N轮 拿取列表第N项，遍历列表前N项（已排序）最大到最小顺序比较后 插入(待移动项依次后移)到正确位置
    """
    i = 1
    while i < len(tlist):
        waitInsert = tlist[i]
        j = i - 1
        while j >= 0:
            if waitInsert < tlist[j]:
                tlist[j + 1] = tlist[j]
                j = j - 1
            else:
                break
        tlist[j + 1] = waitInsert
        i = i + 1
    return tlist

if __name__ == '__main__':
    s = bubbleSort([11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(s)
