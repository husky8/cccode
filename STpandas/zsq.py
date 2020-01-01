
f1 = open("d1.csv",encoding="utf-8")
f2 = open("d11.csv","w",encoding="utf-8")
index = 1
for i in f1.readlines():
    f2.writelines('=HYPERLINK("{}")\n'.format(i.replace("\n","")))
    if index %1000 ==0:
        print(index)
    index = index+1
