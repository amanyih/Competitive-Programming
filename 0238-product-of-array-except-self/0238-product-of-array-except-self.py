class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)
        prev = 1
        
        for i in range(len(nums)):
            cur = nums[i]
            ans[i] = prev
            prev *= cur
        after = 1
        for i in range(len(nums)-1,-1,-1):
            cur = nums[i]
            ans[i] *= after
            after *= cur
        
        
        return ans
        