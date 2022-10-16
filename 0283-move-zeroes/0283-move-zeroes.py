class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        1,3,12,0,0]
               l
                   r
         [1,2,0]
              l
                r
        """
        
        left = 0
        
        right = 0
        
        while left < len(nums) and right < len(nums):
            if nums[left] != 0 and left <= right:
                left += 1
            elif nums[right] == 0 or left > right:
                right += 1
            else:
                
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right += 1
            
        