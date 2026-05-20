class LinkedList:
    
    def __init__(self):
        self.linkL = []

    
    def get(self, index: int) -> int:
        if(index > len(self.linkL) -1):
            return -1
        return self.linkL[index]
        
        

    def insertHead(self, val: int) -> None:
        self.linkL.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        self.linkL.append(val)
        

    def remove(self, index: int) -> bool:
        if(index > len(self.linkL) -1):
            return False
        self.linkL.pop(index)
        return True
        

    def getValues(self) -> List[int]:
        return self.linkL
        
