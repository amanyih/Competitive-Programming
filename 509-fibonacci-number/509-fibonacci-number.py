class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        
        def fibonacci(n):
            if n in cache:
                return cache[n]
            if n == 0 or n == 1:
                return n
            else:
                val = fibonacci(n-1) + fibonacci(n-2)
            
            cache[n] = val
            
            return val
        return fibonacci(n)