# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        preorder.reverse()
        
        def build(x = -inf,y=inf):
            if not preorder:
                return None
            
            node = TreeNode(val = preorder.pop())
            if preorder and preorder[-1] < node.val:
                node.left = build(x,node.val)
            if preorder and (preorder[-1] > x and preorder[-1] < y):
                node.right = build(node.val,y)
            
            return node
        
        return build()
            
        