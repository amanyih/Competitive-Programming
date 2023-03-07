# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        def insertNode(node,value):
            if not node:
                return TreeNode(val=value)
            
            if value < node.val:
                node.left = insertNode(node.left,value)
            elif value > node.val:
                node.right = insertNode(node.right,value)
            
            return node
        return insertNode(root,val)
        