class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # cache = {}
        
        @cache
        def findLIS(index):
            
            ans = 1
            for i in range(index):
                if nums[i] < nums[index]:
                    ans = max(ans,1+findLIS(i))
            return ans
                    
        ans = 1
        for i in range(len(nums)):
            ans = max(ans,findLIS(i))
        return ans