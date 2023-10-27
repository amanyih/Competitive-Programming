class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) -1
   
        while left < right:
            mid = (left + right) // 2
            if (mid % 2 and nums[mid] == nums[mid-1]) or (not mid % 2 and nums[mid] == nums[mid+1]):
                left = mid + 1
            else:
                right = mid
                
        return nums[left]
                
            
              
                      
                 