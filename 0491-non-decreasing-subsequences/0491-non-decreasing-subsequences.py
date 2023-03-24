class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        
        
        def backtrack(path,index):
            # print(path,index)
            if index >= len(nums):
                if len(path) > 1:
                    res.add(tuple(path[:]))
                return            
                
            if path and path[-1] <= nums[index] or not path:
                path.append(nums[index])
                backtrack(path,index+1)
                path.pop()
            backtrack(path,index+1)
        backtrack([],0)
        
        return [list(x) for x in res]