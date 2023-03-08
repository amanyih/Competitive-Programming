# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = [[] for x in range(1000)]
        
        
        def help(node,level):
            if not node:
                return
            
            level += 1
            help(node.left,level)
            levels[level].append(node.val)
            help(node.right,level)
        
        help(root,0)
        return [level for level in levels if level]
        