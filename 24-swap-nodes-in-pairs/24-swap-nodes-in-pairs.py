# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self,head):

        newNode = ListNode(next=head)
        tail = newNode

        prev = head
        while prev and prev.next:
            cur = prev.next
            temp = cur.next
            cur.next = prev
            prev.next = temp
            tail.next = cur
            tail = prev
            prev = temp

        return newNode.next
        