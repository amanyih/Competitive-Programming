# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        count = defaultdict(int)
        global maxCount
        maxCount = -inf
        
        def traverse(node):
            if not node:
                return
            global maxCount
            traverse(node.left)
            count[node.val] += 1
            maxCount = max(maxCount,count[node.val])
            traverse(node.right)
        traverse(root)
        res = []
        for key in count:
            if count[key] == maxCount:
                res.append(key)
        return res