class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        maxLength = trips[0][-1]
        
        for trip in trips:
            if trip[-1] > maxLength:
                maxLength = trip[-1]
        
        prefix = [0] * (maxLength +1)
        
        for trip in trips:
            prefix[trip[1]] += trip[0]
            
            prefix[trip[-1]] -= trip[0]
                
        
        curSum = 0
        
        for i in range(len(prefix)):
            curSum += prefix[i]
            if curSum > capacity:
                return False
        
        return True
            
            