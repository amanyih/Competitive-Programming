class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        left = 1
        right = n
        ans = 1
        while left <= right:
            mid =( left + right) // 2    
            cur_sum = mid * (mid+1) // 2
            if cur_sum == n:
                return mid
            if cur_sum < n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
        
        