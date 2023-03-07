class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        
        
        def sumOfQuotient(divisor):
            res = 0
            
            for num in nums:

                res += (ceil(num/divisor))
            return res
        
    
        left = 1
        right = max(nums)
        
        while left + 1 <= right:
            mid = (right + left) // 2
            
            cur = sumOfQuotient(mid)
            
            if cur <= threshold:
                right = mid
            else:
                left = mid +1
        return right
            
            