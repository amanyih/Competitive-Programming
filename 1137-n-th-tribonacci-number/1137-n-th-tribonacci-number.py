class Solution:
    def tribonacci(self, n: int) -> int:
        
        @cache
        def help(n):
            if n == 1 or n == 2:
                return 1
            elif n == 0:
                return 0
            
            return help(n-1) + help(n-2) + help(n-3)
        
        return help(n)
        