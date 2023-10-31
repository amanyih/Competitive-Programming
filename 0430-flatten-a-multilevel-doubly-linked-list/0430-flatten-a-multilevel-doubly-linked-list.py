"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummyHead = Node()
        dummyHead.next = head
        
        while head:
            # print(head.val)
            if head.child:
                nxt = head.next
                flat_head = self.flatten(head.child)
                flat_head.prev , head.next = head,flat_head
                head.child = None
                tail = self.getTail(flat_head)
                if nxt:
                    nxt.prev = tail
                if tail:
                    tail.next = nxt
                # tail.next,nxt.prev = nxt,tail
                head = nxt
                
            else:
                head = head.next
        
        # print("at head val",head.val)
        # while head:
            
        return dummyHead.next
    def getTail(self,head):
        
        while head.next:
            head = head.next
        return head
        