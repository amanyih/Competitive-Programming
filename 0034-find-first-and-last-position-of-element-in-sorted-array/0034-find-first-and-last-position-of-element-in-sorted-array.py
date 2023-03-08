class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        left = 0
        right = len(nums)-1
        res = [-1,-1]
        
        while left + 1 <= right:
            mid = (left+right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        # print(left)
        if nums[left] == target:
            res[0] = left
        left = 0
        right = len(nums) - 1
        ans = 0

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
                ans = mid
            else:
                right = mid-1
        if nums[ans] == target:
            res[1] = ans
        return res
        
        
        