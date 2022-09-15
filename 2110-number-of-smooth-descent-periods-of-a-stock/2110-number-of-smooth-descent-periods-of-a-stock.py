class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        count = 0
        left = 0
        
        for right in range(len(prices)):
            if right > 0 and prices[right-1] - prices[right] != 1:
                left = right
            
            count += (right - left + 1)
        
        return count
            
        