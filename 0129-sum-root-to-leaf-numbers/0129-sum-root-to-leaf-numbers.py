# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        nums = []
        
        def traverse(node,path):
            if not node.left and not node.right:
                path.append(str(node.val))
                nums.append(int("".join(path)))
                path.pop()
                return
            
            path.append(str(node.val))
            
            if node.left:
                
                traverse(node.left,path)
            if node.right:
                
                traverse(node.right,path)
            
            path.pop()
        traverse(root,[])
        return sum(nums)
        