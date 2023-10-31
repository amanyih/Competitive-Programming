# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        
        q = deque([(root,0)])
        levels = defaultdict(list)
        
        while q:
            
            node,level = q.popleft()
            levels[level].append(node.val)
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        ans = []
        # print(levels)
        for i in range(len(levels)):
            cur = levels[i]
            if not i%2:
                ans.append(cur)
            else:
                # print(cur.reverse())
                # print(cur)
                cur.reverse()
                ans.append(cur)
        
        return ans
                
            
                
            
            
        