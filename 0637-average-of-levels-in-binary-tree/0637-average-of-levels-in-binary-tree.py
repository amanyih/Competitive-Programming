# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        ans = []
        
        
        q = deque([root])
        
        while q:
            
            cur = 0
            for node in q:
                cur += node.val
            ans.append(cur/len(q))
            
            new_q = []
            
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = deque(new_q)
        return ans
        