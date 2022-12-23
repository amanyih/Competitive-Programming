class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        
        minSum = float("inf")
        ans = -1
        
        for i in range(len(points)):
            
            if points[i][0] == x or points[i][1] == y:
                
                x1,y1 = points[i]
                dist = abs(x-x1) + abs(y-y1)
                
                if dist < minSum:
                    minSum = dist
                    ans = i
        
        return ans
        
                    
        