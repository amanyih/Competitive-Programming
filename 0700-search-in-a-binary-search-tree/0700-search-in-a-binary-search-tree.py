# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def findNode(node):
            if not node:
                return None
            
            if node.val < val:
                return findNode(node.right)
            elif node.val > val:
                return findNode(node.left)
            else:
                return node
        return findNode(root)
        