class Solution:
    def climbStairs(self, n: int) -> int:
        
        last = 1
        afterLast = 0
        
        for i in range(n,0,-1):
            
            cur = last + afterLast
            afterLast = last
            last = cur
        
        return last
            
            
            
        
        
        
        