# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(next = head)
        prevNode = dummyNode
        count=0
        tail = head
        while tail:
            count += 1
            if count == k:
                nextNode = tail.next
                tail .next = None
                last = prevNode.next
                prev  = nextNode
                cur = last
                while cur:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
                prevNode.next = prev
                prevNode = last
                count = 0
                tail=nextNode
            else:
                tail = tail.next
        
        return dummyNode.next
                    
                
            
            
        
        
            
            
            
        