class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = 0
        left = 0
        ans = len(nums) + 1
        for right in range(len(nums)):
            curSum += nums[right]
            while curSum >= target:
                ans = min(ans,right - left + 1)
                curSum -= nums[left]
                left += 1
        
        return ans if ans < len(nums) +1 else 0
            