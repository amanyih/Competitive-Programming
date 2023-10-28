# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            prev = None
            
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        
        l1_r = reverse(l1)
        l2_r = reverse(l2)
        
        dummyNode = ListNode()
        tail = dummyNode
        
        carry = 0
        
        while l1_r or l2_r or carry:
            cur = carry
            if l1_r :
                cur += l1_r.val
                l1_r = l1_r.next
            if l2_r:
                cur += l2_r.val
                l2_r = l2_r.next
            
            val = cur % 10
            carry = cur // 10
            tail.next = ListNode(val)
            tail = tail.next
        return reverse(dummyNode.next)
                