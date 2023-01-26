class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        rangee = ceil(sqrt(c))
        
        for i in range(rangee):
            target = sqrt(c - (i**2))
            
            if target <= rangee and target == ceil(target):
                return True
        
        
        return False
         
        