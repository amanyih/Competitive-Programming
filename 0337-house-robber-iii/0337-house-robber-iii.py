# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        #[anc,prev]
        def traverse(node):
            if not node:
                return [0,0]
            
            la,lp = traverse(node.left)
            ra,rp = traverse(node.right)
            
            cur = max(la+ra+node.val,lp+rp)
            
            return [lp+rp,cur]
        
        return max(traverse(root))
            