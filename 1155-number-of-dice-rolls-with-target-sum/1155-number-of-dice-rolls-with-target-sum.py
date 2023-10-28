class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @cache
        def dp(remain,cur):
            
            if remain == 0 and cur == target:
                return 1
            elif remain == 0:
                return 0
            if cur > target:
                return 0
            
            count = 0
            
            for i in range(1,k+1):
                count += dp(remain-1,cur+i)
            
            return count % (10**9 + 7)
    
        return dp(n,0)
                