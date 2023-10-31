"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        level = defaultdict(list)
        
        q = deque([(root,0)])
        
        while q:
            node,l = q.popleft()
            # print(l,"val",node.val)
            level[l].append(node)
            
            if node.left:
                # print("to left")
                q.append((node.left,l+1))
            if node.right:
                q.append((node.right,l+1))
        
        for key in level:
            # print("keyyy",key)
            for i in range(len(level[key])-1):
                node = level[key][i]
                nxt = level[key][i+1]
                # print(node.val,nxt.val,"0-")
                node.next = nxt
        # print(level)
        return level[0][0]
        
        
            
            
        
        