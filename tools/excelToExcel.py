import sqlite3
from tools.operateExcel import readExcel
def excelToSqlite(kv,inPath,outPath=None,stripHandLine=False):

    # if outPath is None: outPath=inPath.split(".")[0]+".db"
    # if ".db" not in outPath:outPath=outPath+".db"
    # con = sqlite3.connect(outPath)
    con = sqlite3.connect("config.db")
    cursor = con.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS countryCode
                (
                    chineseSimpleName TEXT,
                    englishSimpleName TEXT,
                    englishiFullName TEXT,
                    twoLetterCode TEXT,
                    threeLetterCode TEXT,
                    digitalCode TEXT
                );
                ''')

    res_excel = readExcel(inPath)
    skipHandline=True
    for row in res_excel:
        if skipHandline:
            skipHandline=False
            continue
        # print(row)
        # print('''insert into main (chineseSimpleName,englishSimpleName,englishiFullName,twoLetterCode,threeLetterCode,digitalCode)
        #        values({},{},{},{},{},{})'''.format(row[1],row[2],row[3],row[4],row[5],row[6]))
        cursor.execute('''insert into countryCode (chineseSimpleName,englishSimpleName,englishiFullName,twoLetterCode,threeLetterCode,digitalCode) 
               values('{}','{}','{}','{}','{}','{}')'''.format(row[1],row[2],row[3],row[4],row[5],row[6]))
        con.commit()

    s=cursor.execute("SELECT * FROM countryCode")

    print(s.fetchall())





if __name__ == '__main__':

    excelPath = "/Users/smzdm/PycharmProjects/cc/FeatureCenter/doc/国家编码.xlsx"
    kv={"chineseSimpleName":"text",
     "englishSimpleName":"text",
     "englishiFullName":"text",
     "twoLetterCode":"text",
     "threeLetterCode":"text",
     "digitalCode":"text"}
    excelToSqlite(kv,"/Users/smzdm/PycharmProjects/cc/FeatureCenter/doc/国家编码.xlsx")

