# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        def dfs(node,parent = None):
            if not node:
                return
            
            node.parent = parent
            
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root)
        
        q = deque([(target,0)])
        visited = {target}
        
        
        while q:
            
            if q[0][1] == k:
                ans = []
                for node,c in q:
                    ans.append(node.val)
                return ans
            
            cur,cost = q.popleft()
            nxt = [cur.left,cur.right,cur.parent]
            
            for node in nxt:
                if node and node not in visited:
                    visited.add(node)
                    q.append((node,cost+1))
        
        return []
            
            