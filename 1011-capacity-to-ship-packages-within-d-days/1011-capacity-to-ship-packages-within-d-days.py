class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def countDays(capacity):
            count = 1
            cur = 0
            for weight in weights:
                cur += weight
                if cur > capacity:
                    count += 1
                    cur = weight
            return count
                    
        
        left = 0
        right = 0
            
        for weight in weights:
            right += weight
            left = max(weight,left)
        
        while left+1 <= right:
            mid = (right+left) // 2
            
            if countDays(mid) <= days:
                right = mid
            else:
                left = mid + 1
        return right
            
            
            
            