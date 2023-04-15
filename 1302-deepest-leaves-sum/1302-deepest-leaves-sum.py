# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        graph = defaultdict(list)
        
        maxLevel = 0
        def traverse(node,level=0):
            nonlocal maxLevel
            if not node:
                return
            maxLevel = max(maxLevel,level)
            
            graph[level].append(node.val)
            traverse(node.left,level+1)
            traverse(node.right,level+1)
        
        traverse(root)
        
        return sum(graph[maxLevel])