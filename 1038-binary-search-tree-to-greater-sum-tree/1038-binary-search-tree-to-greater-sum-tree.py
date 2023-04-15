# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        num = 0                                   
        
        def traverse(node):
            nonlocal num
            if not node:
                return
            
            traverse(node.right)
            num += node.val
            node.val = num
            traverse(node.left)
            
            return node
        return traverse(root)
            
        