# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        count = 0
        tail= head
        while head:
            count+=1
            head = head.next
        
        ansList = [0]*count
        index = 0
        while tail:
            while stack and stack[-1][0] < tail.val:
                ansList[stack.pop()[1]]= tail.val
                
            
            stack.append([tail.val, index])
            tail=tail.next
            index += 1
            
            
        
        return ansList
                
        
            
        