# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        copyNode = node.next
        node.val= copyNode.val
        node.next = copyNode.next
        copyNode.next = None
        