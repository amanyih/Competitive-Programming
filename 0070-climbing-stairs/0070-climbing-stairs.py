class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def help(cur):
            if cur == 1 or cur == 2:
                return cur
            return help(cur-1) + help(cur - 2)
        
        return help(n)
        
        