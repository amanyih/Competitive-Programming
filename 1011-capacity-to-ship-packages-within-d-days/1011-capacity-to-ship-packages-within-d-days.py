class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canCarryAll(capacity):
            cur = 0
            count = 0
            
            for weight in weights:
                if cur + weight > capacity:
                    cur = 0
                
                if cur == 0:
                    count += 1
                cur += weight
            return count <= days
                   
        left = 0
        right = 0
        
        for weight in weights:
            left = max(left,weight)
            right += weight
        
        while left < right:
            mid = (left + right) // 2
            
            canCarry = canCarryAll(mid)
            if canCarry:
                right = mid
            else:
                left = mid + 1
        return left
            
            
        
        

           
        
            
            
            
            