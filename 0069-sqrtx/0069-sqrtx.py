class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        ans = x
        right = x
        
        while left <= right:
            mid =(right + left) //2 
                          
            if mid * mid > x:
                right = mid-1
            elif mid * mid <= x:
                ans = mid
                left = mid+1
        return ans
        
        