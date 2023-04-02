# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        cur = dummy

        for i in range(left-1):
            cur = cur.next

        ending = cur.next
        curr = ending

        prev = None
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        ending.next = curr
        cur.next = prev

        return dummy.next
        
        
        
            
        