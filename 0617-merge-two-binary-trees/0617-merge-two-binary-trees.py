# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def traverse(root1,root2):
            if not root1 and not root2:
                return None
            newNode = TreeNode()
            left1=left2=right1=right2 = None
            if root1:
                newNode.val += root1.val
                left1 = root1.left
                right1 = root1.right
            if root2:
                newNode.val += root2.val
                left2 = root2.left
                right2 = root2.right
            
            newNode.left = traverse(left1,left2)
            newNode.right = traverse(right1,right2)
            
            return newNode
        
        return traverse(root1,root2)