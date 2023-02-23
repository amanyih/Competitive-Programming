# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        smaller = ListNode()
        larger = ListNode()
        s = smaller
        l = larger
        
        curHead = head
        
        while curHead:
            if curHead.val < x:
                s.next = ListNode(val=curHead.val)
                s = s.next
            else:
                l.next = ListNode(val = curHead.val)
                l = l.next
            curHead = curHead.next
        s.next = larger.next
        return smaller.next
            
        
                
                
        
        
        