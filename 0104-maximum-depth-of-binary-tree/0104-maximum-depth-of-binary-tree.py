# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            if not node:
                return 0
            
            left = 0
            right = 0
            
            left += traverse(node.left)
            right += traverse(node.right)
            
            return max(left,right) + 1
            
        return traverse(root)
            
        