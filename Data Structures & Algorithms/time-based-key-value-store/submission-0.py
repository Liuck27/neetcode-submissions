class TimeMap:

    from collections import defaultdict

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:

        lista = self.store[key]
        res = ""

        l = 0
        r = len(lista)-1

        while l<=r:
            m = (l+r)//2
            if lista[m][0] > timestamp:
                r = m - 1
            else:
                res = lista[m][1]
                l = m + 1

        return res

        
