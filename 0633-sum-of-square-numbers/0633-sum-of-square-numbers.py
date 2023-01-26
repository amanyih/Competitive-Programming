class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        rangee = ceil(sqrt(c))
        nums = [i for i in range(rangee+1)]
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            sqLeft = nums[left] **2
            sqRight = nums[right] ** 2
            
            res = sqLeft + sqRight
            
            if res > c:
                right -= 1
            elif res < c:
                left += 1
            else:
                return True
        return False
         
        