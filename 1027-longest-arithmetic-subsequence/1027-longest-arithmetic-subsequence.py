class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        cache = {}
        
        for i in range(len(nums)):
            for j in range(0,i):
                cache[(i,nums[i]-nums[j])] = cache.get((j,nums[i]-nums[j]),1) + 1
        
        return max(cache.values())