# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dictt = {}
        while headA:
            dictt[headA] = headA
            headA = headA.next
        
        while headB:
            if headB in dictt:
                return headB
            else:
                headB = headB.next
        
        return None
        
        