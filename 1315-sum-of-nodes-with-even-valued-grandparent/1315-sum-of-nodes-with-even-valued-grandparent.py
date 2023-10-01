# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(node,p=1,gp=1):
            if not node:
                return 0
            
            count = 0
            if not gp%2:

                count += node.val
            count += dfs(node.left,node.val,p) + dfs(node.right,node.val,p)
            
            return count
        
        return dfs(root)
            
            
        