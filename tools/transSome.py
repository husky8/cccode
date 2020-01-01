
class TransSome():
    def dicListStr2Int(self,dic):
        res = {}
        for i in dic.keys():
            res[i] = [int(j) for j in dic[i] ]
        return res

if __name__ == '__main__':
    dic = {'4': ['2856', '4856', '6856', '8856', '0856', '9956'], '6': ['432293', '932293', '692017'], '7': ['4675884', '6675884', '8675884', '2675884', '0675884'], '8': ['09530427', '34530427', '59530427', '84530427'], '9': ['047423135']}
    TransSome().dicListStr2Int(dic)