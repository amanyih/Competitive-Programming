# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        tail = head
        
        count = 0
        
        while head:
            count += 1
            head = head.next
        
        
        ans = []
        cur = 0
        total = 0
        
        while tail:
            if cur == 0:
                ans.append(tail)
                total += 1
            
            cur += 1
            
            
            if  total <= count % k:
                if cur == count // k + 1:
                    nxt = tail.next
                    tail.next = None
                    cur = 0
                    tail = nxt
                else:
                    tail = tail.next
            else:
                if cur == count // k:
                    nxt = tail.next
                    tail.next = None
                    cur = 0
                    tail = nxt
                else:
                    tail = tail.next
        while len(ans) < k:
            ans.append(None)
        return ans
                
                
            
        