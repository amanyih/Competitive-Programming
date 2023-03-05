class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        right = max(piles)
        left = 1
        
        def hoursTaken(speed):
            hours = 0
            for pile in piles:
                hours += ceil(pile/speed)
            return hours
        
        
        while left +1  <= right:
            mid = (left + right) //2
            
            if hoursTaken(mid) <= h:
                right = mid
            else:
                left = mid + 1
        
        return right
            
            
        
        