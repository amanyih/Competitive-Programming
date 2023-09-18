class Solution:
    def minSteps(self, n: int) -> int:
        
        
        def findFactor(n):
            
            for i in range(n-1,int(sqrt(n))-1,-1):
                if n % i == 0:
                    return i
            return 1
        
        def find(n):
            if n == 1:
                return 0
            if n <=5:
                return n
            
            factor = findFactor(n)
             
            return find(factor) + n//factor
        return find(n)
        
        