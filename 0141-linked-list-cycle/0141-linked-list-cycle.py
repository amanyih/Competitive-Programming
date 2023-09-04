 #Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
            self.val = x
            self.next = None

class Solution:
    def hasCycle(self, node: Optional[ListNode]) -> bool:
        if not node or not node.next or not node.next.next: return False
        
        fast = node.next.next
        slow = node.next
        
        while slow and fast and fast.next:
            if slow == fast:
                return True
            fast = fast.next.next
            slow = slow.next
        
        return False
            