# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newNode = ListNode(next= head)
        
        while head and head.next:
            temp = head.next
            while temp and head.val == temp.val:
                temp = temp.next
            head.next = temp
            head = head.next
        return newNode.next
        