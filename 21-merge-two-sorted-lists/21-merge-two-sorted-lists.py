# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        ansNode = ListNode()
        head = ansNode
        
        while head1 and head2:
            if head1.val < head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            
            head = head.next
        
        if head1:
            head.next = head1
        elif head2:
            head.next = head2
            
        
        return ansNode.next
            
                
                    
                
            
            
            
        
        
        