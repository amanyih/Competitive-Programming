# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(next = head)
        tail = dummyHead
        
        first = head
        
        for i in range(n):
            first = first.next
        
        while first:
            first = first.next
            tail = tail.next
        
        nxt = tail.next.next
        tail.next = nxt
        
        return dummyHead.next
        
        
        
                
        
        