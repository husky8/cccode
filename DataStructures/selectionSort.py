def selectionSort(tlist):
    """
    复杂度 O^2
    选择排序 假定第一项为最小，遍历后续列表，如有最小替换索引，直至结束，若index !=0 交换位置
    """
    i = 0
    while i < len(tlist) - 1:
        minIndex = i
        j = i + 1
        while j < len(tlist):
            if tlist[j] < tlist[minIndex]:
                minIndex = j
            j = j + 1
        if minIndex != i:
            tlist[minIndex], tlist[i] = tlist[i], tlist[minIndex]
        i = i + 1
    return tlist


if __name__ == '__main__':
    s = selectionSort([1, 5, 6, 4, 8, 9, 6, 5, 4, 7, 5, 1, 3])
    print(s)
