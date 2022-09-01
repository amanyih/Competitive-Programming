# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ansList = []
        index = 0
        while head:
            ansList.append(0)
            while stack and stack[-1][0] < head.val:
                ansList[stack.pop()[1]]= head.val
                
            
            stack.append([head.val, index])
            head=head.next
            index += 1
            
            
        
        return ansList
                
        
            
        