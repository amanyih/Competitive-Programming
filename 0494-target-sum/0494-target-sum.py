class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        
        
        def backtrack(index,curSum):
            if index == len(nums):
                if curSum == target:
                    return 1
                return 0
            if (index,curSum) in dp:
                return dp[(index,curSum)]
            
            dp[(index,curSum)] = backtrack(index+1,curSum+nums[index]) + backtrack(index+1,curSum -nums[index])
            
            return dp[(index,curSum)]
        
        return backtrack(0,0)
        
            
            
                
            
        