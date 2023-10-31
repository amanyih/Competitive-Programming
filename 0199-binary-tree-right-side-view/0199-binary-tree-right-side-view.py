# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        levels = defaultdict(list)
        
        q = deque([(root,0)])
        
        while q:
            node,level = q.popleft()
            
            levels[level].append(node.val)
            
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        
        ans = []
        for i in range(len(levels)):
            ans.append(levels[i][-1])
        
        return ans
        
        