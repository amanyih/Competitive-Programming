# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        slow = prev.next
        prev.next = None
        
        left = self.sortList(head)
        right =self.sortList(slow)
        return self.merge(left,right)
        
    
    def merge(self,head1,head2):
        newNode = ListNode()
        tail = newNode
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2
        
        return newNode.next
            