class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] *n
        
        for booking in bookings:
            
            prefix[booking[0]-1] += booking[-1]
            if booking[1] < n:
                prefix[booking[1]] -= booking[-1]
        
        cur = 0
        
        for i in range(n):
            cur += prefix[i]
            prefix[i] = cur
        
        return prefix
            