class Solution:
    def fib(self, n: int) -> int:
        
        @cache
        def help(n):
            
            if n == 1 or  n == 0:
                return n
            
            return help(n-1) + help(n-2)
        
        return help(n)
            
        