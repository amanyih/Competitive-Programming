# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = -inf
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            ans = max(ans,left+right+node.val)
            
            cur = max(0,left+node.val,right+node.val)
            return cur
        dfs(root)
        return ans
            
            
        