class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = {0:0,1:0,2:0}
        
        for num in nums:
            count[num] = count.get(num) + 1
            
        for i in range(len(nums)):
            if count[0] != 0:
                nums[i] = 0
                count[0] = count.get(0) - 1
            elif count[1] != 0:
                nums[i] = 1
                count[1] = count.get(1) - 1
            else:
                nums[i] = 2
                count[2] = count.get(2) - 1
                