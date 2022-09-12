# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None
        ans = 0
        while fast:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        while prev:
            summ = prev.val + nxt.val
            ans = max(ans,summ)
            prev,nxt = prev.next,nxt.next
        
        
        return ans