class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        
        def help(n):
            
            if n in memo:
                return memo[n]
            
            if n <= 2:
                return n
            
            
            memo[n] = help(n-1) + help(n-2)
            
            return memo[n]
        
        
        return help(n)
        
        