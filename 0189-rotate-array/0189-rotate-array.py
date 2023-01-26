class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        copyNums = [i for i in nums]
        for index in range(len(nums)):
            newIndex = (index+k) % len(nums)
            nums[newIndex] = copyNums[index]
            
        