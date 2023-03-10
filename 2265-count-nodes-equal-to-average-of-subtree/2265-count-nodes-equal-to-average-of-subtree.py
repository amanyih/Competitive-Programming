# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:


        count = []
        # [sum,count]
        def traverse(node):
            if not node:
                return [0,0]
            
            left = traverse(node.left)
            right = traverse(node.right)
            curSum = left[0] + right[0] + node.val
            num = left[1]+right[1] + 1
            avg = curSum//(num)
            
            if avg == node.val:
                count.append(1)
            
            return [curSum,num]
        
        traverse(root)
        return sum(count)
        
