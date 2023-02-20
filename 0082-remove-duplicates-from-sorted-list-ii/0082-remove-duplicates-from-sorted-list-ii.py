# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummyHead = ListNode()
        left = dummyHead
        secLeft = head
        right = head
        
        count = 0
        
        while right:
            if secLeft.val != right.val:
                if count == 1:
                    left.next = secLeft
                    left = left.next
                    left.next = None
                secLeft = right
                count = 0
            count += 1
            if not right.next and count == 1:
                left.next = right
            
            right = right.next
            
                
            
        return dummyHead.next
        
        
        