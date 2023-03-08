# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            lst.append(node.val)
            traverse(node.right)
        traverse(root)
        return lst[k-1]
        