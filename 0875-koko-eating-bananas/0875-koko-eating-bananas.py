class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        
        def hoursTaken(speed):
            total_time_taken = 0
            
            for pile in piles:
                total_time_taken += ceil(pile/speed)
            return total_time_taken
            
        
        while left < right:
            mid = (left + right) // 2
            total_time = hoursTaken(mid)
            
            if total_time > h:
                left = mid + 1
            else:
                right = mid
        return right
            
        
        
            
        
        