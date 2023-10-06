# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        cur_path = []
        
        def traverse(node,curSum=0):
            if not node:
                return
                    
            cur_path.append(node.val)
            cur = curSum + node.val
            if not node.left and not node.right and cur == targetSum:
                ans.append(cur_path[:])
                cur_path.pop()
                return
            traverse(node.left,cur)
            traverse(node.right,cur)
            
            cur_path.pop()
            
        traverse(root)
        return ans
            
        