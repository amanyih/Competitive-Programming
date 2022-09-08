# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        newNode = ListNode()
        tail = newNode
        
        first = head
        
        while first:
            count = 0
            temp = first
            while temp and temp.val == first.val:
                count += 1
                temp = temp.next
            if count == 1:
                tail.next = ListNode(val = first.val)
                tail= tail.next
            first = temp
        
        return newNode.next
                
        