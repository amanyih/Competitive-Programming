# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        global count
        count = 0
        seen = defaultdict(int)
        seen[0] = 1
        
        def traverse(node,cur = 0):
            global count
            if not node:
                return
            
            cur_val = cur + node.val
            count += seen[cur_val-targetSum]
            seen[cur_val] += 1
            traverse(node.left,cur_val)
            traverse(node.right,cur_val)
            seen[cur_val] -= 1
            
        traverse(root)
        return count
            