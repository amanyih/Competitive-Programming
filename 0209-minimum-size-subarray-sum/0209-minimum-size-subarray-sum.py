class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ans = len(nums) + 1
        curSum =0
        
        for right in range(len(nums)):
            curSum += nums[right]
            
            while curSum >= target:
                ans = min(ans,right-left+1)
                curSum -= nums[left]
                left += 1
        ans = 0 if ans > len(nums) else ans
        return ans
            
            
        