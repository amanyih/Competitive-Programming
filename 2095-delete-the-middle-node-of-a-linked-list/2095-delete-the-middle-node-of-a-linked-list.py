# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(next=head)
        if head.next == None:
            return None
        
        
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next

        return dummyNode.next
        
        