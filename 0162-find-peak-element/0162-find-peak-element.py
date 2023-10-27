class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left = 0  
        right = len(nums) -1
        
        while left < right:
            
            mid = (left + right) // 2
            left_num = nums[mid-1] if mid - 1 >=0 else -inf
            right_num = nums[mid+1] if mid + 1 < len(nums) else inf
            
            if nums[mid] >  left_num and nums[mid] > right_num:
                return mid
            
            if nums[mid] > left_num:
                left = mid + 1
            else:
                right = mid -1
        return left