# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        
        def count(node,prev = -inf):
            if not node:
                return
            
            if node.val >= prev:
                self.count += 1
            cur_max = max(prev,node.val)
            count(node.left,cur_max)
            count(node.right,cur_max)
        count(root)
        return self.count
            
        