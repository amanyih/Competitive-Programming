class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        
        left = 0
        
        ans = 0
        cur = 0
        
        for right in range(len(nums)):
            cur += nums[right]
            
            while left < right and cur * (right-left+1) >= k:
                cur -=nums[left]
                left += 1
            
            ans += right - left + 1 if (left < right or nums[right] < k) else 0
        
        return ans
            
            
        