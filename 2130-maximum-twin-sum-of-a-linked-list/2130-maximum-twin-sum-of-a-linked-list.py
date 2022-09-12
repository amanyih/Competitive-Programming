# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        stack = []
        
        tail = head
        ans = 0
        while tail:
            stack.append(tail.val)
            tail = tail.next
        
        while head:
            summ = stack.pop() + head.val
            
            ans = max(ans,summ)
            
            head = head.next
        
        return ans