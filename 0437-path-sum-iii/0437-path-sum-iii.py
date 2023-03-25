# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        global count
        global target
        target = targetSum
        count = 0
        
        def traverse(node,seen,curSum):
            global count
            global target
            if not node:
                return
            
            
            # print("here",seen[target-node.val],"node.val",node.val)
            curSum += node.val
            count += seen[curSum-target]
            curSeen = seen.copy()
            curSeen[curSum] += 1
            
            traverse(node.left,curSeen,curSum)
            traverse(node.right,curSeen,curSum)
        intial = defaultdict(int)
        intial[0] += 1
        traverse(root,intial,0)
        return count
        