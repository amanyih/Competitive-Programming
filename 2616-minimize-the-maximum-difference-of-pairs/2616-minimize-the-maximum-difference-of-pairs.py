class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def isValid(diff):
            count = 0
            i = 0
            
            while i < len(nums) -1:
                if abs(nums[i]-nums[i+1]) <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    return True
            return False
        if p == 0: return 0
        
        left = 0
        right = 10 ** 9
        ans = 0
        
        while left <= right:
            mid =( left + right ) // 2
            
            if isValid(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
        
        