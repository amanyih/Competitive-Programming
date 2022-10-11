class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zeros = 0
        ans = 0
        
        left = 0 
        
        for right in range(len(nums)):
            zeros += 1 if nums[right] == 0 else 0
            
            while zeros >1:
                if nums[left] == 0:
                    zeros -= 1
                
                left += 1
            
            ans = max(ans,right - left)
        
        
        return ans
        
        