import openpyxl


def readExcel(path):
    wb=openpyxl.load_workbook(path)
    ws = wb['sheet']
    res=[]
    for row in ws.rows:
        rowRes=[]
        for cell in row:
            # print(cell.value)
            rowRes.append(cell.value)
        res.append(rowRes)
    return res
if __name__ == '__main__':
    r = read("/Users/smzdm/PycharmProjects/cc/FeatureCenter/doc/国家编码.xlsx")
    print( r )