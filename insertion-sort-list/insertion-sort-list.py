# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode(next=head)
        
        
        prev = head
        current = head.next
        
        while current:
            if current.val >= prev.val:
                prev= current
                current = current.next
                continue
            
            first = newNode
            while first.next.val<current.val:
                first= first.next
            
            prev.next = current.next
            current.next =  first.next
            first.next = current
            current = prev.next
        
        return newNode.next
            
            
                
            
             
            
            
        
            
            
            
        
        