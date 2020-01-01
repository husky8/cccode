def bubbleSort(tlist):
    """
    复杂度 O^2
    两两交换，将数值大的放到最后，第一轮冒出最大值至末位，第二轮冒出倒数第二大，以此类推
    """
    n = len(tlist)
    while n > 1:
        i = 1
        flag = False
        while i < n:
            if tlist[i] < tlist[i - 1]:
                tlist[i], tlist[i - 1] = tlist[i - 1], tlist[i]
                flag = True
            i = i + 1
        n = n - 1
        if not flag:
            return tlist
    return tlist


if __name__ == '__main__':
    s = bubbleSort([11,1,2,3,4,5,6,7,8,9,10])
    print(s)
