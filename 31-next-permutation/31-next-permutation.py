class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = len(nums) - 2
        
        while left >= 0 and nums[left+1] <= nums[left]:
            left -= 1
        
        
        if left >= 0:
            right = len(nums) -1
            
            while nums[right] <= nums[left]:
                right -=1
            
            nums[right],nums[left] = nums[left],nums[right]
        
        
        l = left + 1
        r = len(nums) -1
        
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r -= 1
                
                
            
            