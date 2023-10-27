# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        
        ans = []
        
        def traverse(node,path):
            if not node:
                return
            if not node.left and not node.right:
                path.append(str(node.val))
                ans.append("->".join(path))
                path.pop()
                return 
            path.append(str(node.val))
            traverse(node.left,path)
            traverse(node.right,path)
            path.pop()
        
        traverse(root,[])
        return ans
        