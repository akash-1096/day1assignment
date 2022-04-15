from itertools import combinations

class StringClass :

    def __init__(self, strIn):
        self.strVal=strIn


    def strLength(self):
        return len(self.strVal)

    def strToList(self):

        return list(self.strVal)

class PairsPossible:

    def __init__(self,li):
        self.pairs=li


    def pairsFormed(self):
        return list(combinations(self.pairs, 2))


obj1 = StringClass('12314532')

print(obj1.strLength())
print(obj1.strToList())

obj2= PairsPossible(obj1.strToList())

print(obj2.pairsFormed())