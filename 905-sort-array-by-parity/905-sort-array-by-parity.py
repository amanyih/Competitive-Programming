class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[left] % 2 == 0:
                left += 1
                right += 1
            elif nums[right] % 2 == 0:
                nums[left],nums[right] = nums[right],nums[left]
                left+= 1
                right += 1
            else:
                right += 1
        
        return nums
            
    
        