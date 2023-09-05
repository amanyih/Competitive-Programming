"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy = Node(0)
        tail = dummy
        nodemap = {None:None}

        cur = head
        while cur:
            if cur not in nodemap:
                nodemap[cur] = Node(cur.val)
            
            cur = cur.next
        while head:
            copyied = nodemap[head]
            copyied.next = nodemap[head.next]
            copyied.random = nodemap[head.random]
            
            tail.next = copyied
            tail = tail.next
            head = head.next
        
        return dummy.next

        