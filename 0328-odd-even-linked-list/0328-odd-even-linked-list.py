# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummyNode = ListNode(next = head)
        nex = head.next
        prev = None
        count = 1
        
        while head:
            nxt = head.next
            head.next = nxt.next if nxt else nxt
            if count % 2:
                prev = head
            head = nxt
            count += 1
        prev.next = nex
        return dummyNode.next
        
        