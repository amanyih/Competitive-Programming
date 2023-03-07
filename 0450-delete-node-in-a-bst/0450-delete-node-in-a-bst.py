# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def getSuccessor(node):
            n = node
            
            while(n.left):
                n = n.left
            return n
            
        
        def deleteNode(node,key):
            if not node:
                return node
            
            if node.val > key:
                node.left = deleteNode(node.left,key)
            elif node.val < key:
                node.right = deleteNode(node.right,key)
            else:
                # print(node)
                if not node.right and not node.left:
                    node = None
                elif not node.right and node.left:
                    node = node.left
                elif not node.left and node.right:
                    node = node.right
                else:
                    successor = getSuccessor(node.right)
                    node.val = successor.val
                    node.right = deleteNode(node.right,node.val)
                    
            return node
        return deleteNode(root,key)
                
        