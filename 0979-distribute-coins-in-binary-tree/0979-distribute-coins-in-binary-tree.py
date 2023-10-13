# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        
        self.ans = 0
        def search(node):
            if not node:
                return []
            left = search(node.left)
            right = search(node.right)
            negatives = []
            positives = []
            for dist,val in left:
                if val < 0:
                    heappush(negatives,(dist+1,val))
                elif val > 0:
                    heappush(positives,(dist+1,val))
            for dist,val in right:
                if val < 0:
                    heappush(negatives,(dist+1,val))
                elif val > 0:
                    heappush(positives,(dist+1,val))
            if node.val - 1 > 0:
                heappush(positives,(0,node.val-1))
            elif node.val - 1 < 0:
                heappush(negatives,(0,-1))
            # print(node.val,negatives,positives)
            while negatives and positives:
                n_d,n_v = heappop(negatives)
                d_d,d_v = heappop(positives)
                cur = n_v + d_v
                
                self.ans += n_d + d_d
                
                if cur > 0:
                    heappush(positives,(d_d,cur))

            return negatives + positives
        search(root)
        return self.ans
                    
                
                
            
                
            
            
            
        