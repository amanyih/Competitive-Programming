# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        tail = newNode
        
        left = 0
        
        while l1 or l2 or left:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            num = num1 + num2 + left
            left = num //10
            num = num % 10
            
            tail.next = ListNode(val = num)
            tail = tail.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        
        
        return newNode.next
            
                
                