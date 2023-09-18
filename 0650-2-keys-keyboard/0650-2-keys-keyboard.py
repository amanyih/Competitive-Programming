class Solution:
    def minSteps(self, n: int) -> int:
        
        cache = {1 :0,2:2}
        
        def findFactor(n):
            
            for i in range(n-1,int(sqrt(n))-1,-1):
                if n % i == 0:
                    return i
            return 1
        
        def find(n):
            if n in cache:
                return cache[n]
            
            factor = findFactor(n)
             
            cur = find(factor) + n//factor
            cache[n] = cur
            return cur
        return find(n)
        
        