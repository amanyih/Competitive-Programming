# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        graph = defaultdict(list)
        
        def traverse(node,level=0):
            if not node:
                return
            
            graph[level].append(node.val)
            traverse(node.left,level+1)
            traverse(node.right,level+1)
        
        traverse(root)
        
        return [max(graph[key]) for key in sorted(graph)]
        