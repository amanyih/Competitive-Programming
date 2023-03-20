# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = defaultdict(list)
        
        def traverse(node,row=0,col=0):
            if not node:
                return
            
            traverse(node.left,row+1,col-1)
            
            # levels[col][levels[row]].append(node.val)
            # print("here",row,col,levels[col].get(row,[]))
            
            levels[col].append((row,node.val))
            
            traverse(node.right,row+1,col+1)
        
        traverse(root)
        ans = []
        
        for key in sorted(levels):
            lst = levels[key]
            
            lst.sort()
            ans.append([t[1] for t in lst])
        
        return ans
        
        # res = []
        # for col in sorted(levels):
        #     rows = levels[col]
        #     for row in sorted(rows):
        #         level = rows[row]
        #         level.sort()
        #         res.append(level)
        # return res
                
            
        
        