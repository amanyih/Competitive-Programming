# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ansNode = ListNode(next=head)
        last = ansNode
        first = head
        
        for i in range(n):
            first = first.next
        
        while first:
            last = last.next
            first = first.next
        
        last.next = last.next.next
        
        return ansNode.next
        
        
        
                
        
        