# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            
        count = defaultdict(list)
        
        def traverse(node,level=0,parent=0):
            if not node:
                return
            
            traverse(node.left,level+1,2*parent+1)
            count[level].append(parent)
            traverse(node.right,level+1,2*parent+2)
        traverse(root)
        maxWidth = -inf
        for level in count:
            maxWidth = max(maxWidth,max(count[level])-min(count[level]))
        # print(count)
        return maxWidth +1