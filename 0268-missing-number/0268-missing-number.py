class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            while nums[i] != i and nums[i] < len(nums):
                nxt = nums[i]
                nums[i], nums[nxt] = nums[nxt], nums[i]

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        