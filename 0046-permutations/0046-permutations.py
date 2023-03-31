class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        global visited
        visited = 0
        
        
        def backtrack(path):
            global visited
            
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                mask = 1 << (i)
                if visited & mask == 0:
                    path.append(nums[i])
                    visited += mask
                    backtrack(path)
                    path.pop()
                    visited -= mask
        backtrack([])
        return res
                    
        
        
        
        
        