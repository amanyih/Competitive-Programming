# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res  = []
        
        def traverse(path,node):
            if not node:
                return
            elif not node.right and not node.left:
                path.append(str(node.val))
                res.append(path[:])
                path.pop()
                return
            
            path.append(str(node.val))
            traverse(path,node.left)
            traverse(path,node.right)
            path.pop()
        
        traverse([],root)
        for i in range(len(res)):
            res[i] = "->".join(res[i])
        
        return res