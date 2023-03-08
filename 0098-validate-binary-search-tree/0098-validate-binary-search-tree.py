# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = []
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            lst.append(node.val)
            traverse(node.right)
        traverse(root)
        
        for i in range(1,len(lst)):
            if lst[i] <= lst[i-1]:
                return False
        return True
                