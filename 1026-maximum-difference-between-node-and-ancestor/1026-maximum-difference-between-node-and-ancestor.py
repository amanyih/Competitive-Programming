# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        
        
        def findMaxDiff(node,minimum,maximum):
            
            if not node:
                return
            
            self.ans = max(self.ans,abs(node.val-minimum),abs(node.val-maximum))
            
            new_min = min(node.val,minimum)
            new_max = max(node.val,maximum)
            
            findMaxDiff(node.left,new_min,new_max)
            findMaxDiff(node.right,new_min,new_max)
            
        findMaxDiff(root,root.val,root.val)
        
        return self.ans
        