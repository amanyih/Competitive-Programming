class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        
        for booking in bookings:
            ans[booking[0] - 1] += booking[-1]
            if booking[1] < n:
                ans[booking[1]] -= booking[-1]
        
        curSum = 0
        
        for i in range (n):
            curSum += ans[i]
            ans[i] = curSum
        
        return ans