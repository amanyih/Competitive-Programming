# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        head1 = head
        while head:
            stack.append(head.val)
            head = head.next
        
        while head1:
            if stack and stack[-1] == head1.val:
                stack.pop()
                head1 = head1.next
            else:
                return False
        
        return True
        