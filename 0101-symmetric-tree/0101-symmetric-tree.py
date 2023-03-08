# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root1,root2):
            if not root1 and not root2:
                return True
            elif (not root1 and root2) or (not root2 and root1):
                return False
            elif root1.val != root2.val:
                return False
            
            path1 = traverse(root1.left,root2.right)
            path2 = traverse(root1.right,root2.left)
            
            return path1 and path2
        
        return traverse(root,root)
        
            
        
        
        
        
        