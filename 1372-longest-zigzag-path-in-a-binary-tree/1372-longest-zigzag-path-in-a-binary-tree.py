# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        def traverse(node,direction=None,cur=0):
            nonlocal ans
            if not node:
                return
            
            ans = max(ans,cur)
            
            leftCur = 1
            rightCur= 1
            
            if direction != "left":
                leftCur += cur
            if direction != "right":
                rightCur += cur
            
            traverse(node.left,"left",leftCur)
            traverse(node.right,"right",rightCur)
        
        traverse(root)
        return ans
                