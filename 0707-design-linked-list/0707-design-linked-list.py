class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode

        
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode()

    def get(self, index: int) -> int:
        if index >= self.size: return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.next.val
        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        newNode = ListNode(val)
        newNode.next = curr.next
        curr.next = newNode
        self.size += 1
   
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)