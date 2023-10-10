# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        hashmap = defaultdict(int)
        ans = []
        
        def dfs(node):
            if not node:
                return []  
            cur = [str(node.val)] +["l"]+ dfs(node.left) +["r"]+ dfs(node.right)
            cur_str = "*".join(cur)
            if hashmap[cur_str] == 1:
                ans.append(node)
            hashmap[cur_str] += 1
            
            return cur
        dfs(root)
        return ans
            
            
            
        