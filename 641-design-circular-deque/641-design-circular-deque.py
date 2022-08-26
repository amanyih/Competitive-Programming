class MyCircularDeque:

    def __init__(self, k: int):
        self.qeue=[]
        self.len=k
        

    def insertFront(self, value: int) -> bool:
        if(len(self.qeue)==self.len):
            return False
        else:
            self.qeue.insert(0,value)
            return True

        
        
        

    def insertLast(self, value: int) -> bool:
        if(len(self.qeue)==self.len):
            return False
        self.qeue.append(value)
        return True
        

    def deleteFront(self) -> bool:
        if(len(self.qeue)==0):
            return False
        self.qeue.pop(0)
        return True
        

    def deleteLast(self) -> bool:
        if(len(self.qeue)==0):
            return False
        self.qeue.pop(-1)
        return True

    def getFront(self) -> int:
        if(len(self.qeue)!=0):
            return self.qeue[0]
        return -1
        

    def getRear(self) -> int:
        if(len(self.qeue)!=0):
            return self.qeue[-1]
        return -1
     

    def isEmpty(self) -> bool:
        if(len(self.qeue)==0):
            return True
        return False
        

    def isFull(self) -> bool:
        if(len(self.qeue)==self.len):
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()