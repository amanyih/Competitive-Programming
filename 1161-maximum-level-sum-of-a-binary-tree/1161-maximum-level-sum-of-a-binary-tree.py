# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque(([(root,1)]))
        
        level_sum = defaultdict(int)
        res = (1,root.val)
        
        while q:
            
            node,level = q.popleft()
            
            level_sum[level] += node.val
            
            if node.right:
                q.append((node.right,level+1))
            if node.left:
                q.append((node.left,level+1))
        
        for key in level_sum:
            if level_sum[key] > res[1]:
                res = (key,level_sum[key])
        return res[0]
            
            
        