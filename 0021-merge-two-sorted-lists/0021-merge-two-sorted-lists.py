# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        elif not list2 and not list1:
            return None
        
        
        
        node = ListNode()
        
        if list1.val <= list2.val:
            node.val = list1.val
            list1 = list1.next
        else:
            node.val = list2.val
            list2 = list2.next
        
        node.next = self.mergeTwoLists(list1,list2)
        
        return node