 #Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
            self.val = x
            self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False
        if head.next == None: return False
        if head.next.next == None: return False
        
        first = head.next.next
        second = head.next
        
        while first != None and second != None:
            if (first == second):
                return True
            elif first.next == None or second.next == None:
                return False
            else:
                first = first.next.next
                second = second.next
            