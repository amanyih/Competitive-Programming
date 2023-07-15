class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def help(nums):
            anc = 0
            prev = 0      
            for num in nums:
                temp = prev
                prev = max(anc+num,prev)
                anc = temp
            return max(anc,prev)
        
        return max(help(nums[:len(nums)-1]),help(nums[1:]))