# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        arr = [None] * 100

        def traverse(node,level = 0):
            
            if not node:
                return
           
            traverse(node.left,level+1)
            # print(level,node.val)
            arr[level] = node.val
            # print(visited)
            traverse(node.right,level+1)
        traverse(root)
        res = [x for x in arr if x != None]
            
        return res
        