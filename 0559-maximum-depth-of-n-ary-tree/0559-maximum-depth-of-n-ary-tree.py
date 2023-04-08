"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        global ans
        ans = 0
        
        def traverse(node,level = 1):
            global ans
            # print("level",level,"val",node.val)
            
            if not node:
                
                return
            ans = max(ans,level)
            for n in node.children:
                traverse(n,level + 1)
        
        traverse(root)
        return ans
            
        