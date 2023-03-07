# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = set()
        
        def traverse(node,key,last = None):
            if not node:
                return
            if node in ans:
                last = node
                # print("found")
                # print(node)
            else:
                ans.add(node)
            
            if key.val < node.val:
                return traverse(node.left,key,last)
            elif key.val > node.val:
                return traverse(node.right,key,last)
            
            return last
        traverse(root,p)
        # for node in ans:
        #     print("------------")
        #     print(node)
        return traverse(root,q)
                
                
        