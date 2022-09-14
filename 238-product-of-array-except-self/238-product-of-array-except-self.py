class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        ans = []
        for i in range(len(nums)):
            ans.append(prefix)
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans
            
        