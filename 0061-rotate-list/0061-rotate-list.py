# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummyNode = ListNode(next=head)
        length = 1
        
        while head.next:
            length += 1
            head = head.next
        last = head
        k = k % length
        if k == 0:
            return dummyNode.next
        iteration = 0
        head = dummyNode.next
        ref = head
        prev = None
        while iteration < length - k:
            prev = head
            head = head.next
            iteration += 1
        prev.next = None
        dummyNode.next = head
        last.next = ref
        return dummyNode.next
        
            
        
        
        
            
        
        