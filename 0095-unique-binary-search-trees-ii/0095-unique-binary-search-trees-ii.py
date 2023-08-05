# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def backtrack(arr):
            # print(arr)
            if len(arr) == 0:
                return []
            
            res = []
            
            for i in range(len(arr)):
                # print("choosen head",i)
                
                
                left = backtrack(arr[:i])
                right = backtrack(arr[i+1:])
                
                if len(right) == 0 and len(left) == 0:
                    res.append(TreeNode(val = arr[i]))
                elif len(right) == 0:
                    for j in range(len(left)):
                        head = TreeNode(val = arr[i])
                        head.left = left[j]
                        res.append(head)
                elif len(left) == 0:
                    for j in range(len(right)):
                        head = TreeNode(val=arr[i])
                        head.right = right[j]
                        res.append(head)
                else:
                    for j in range(len(left)):
                        for k in range(len(right)):
                            head = TreeNode(val = arr[i])
                            head.left = left[j]
                            head.right = right[k]
                            
                            res.append(head)
            # print("return",res)
            return res
        
        return backtrack([i+1 for i in range(n)])
                        
                
                
                
                    
                    
        