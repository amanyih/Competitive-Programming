class Solution:
    def countOrders(self, n: int) -> int:
        
        dp = {1:1}
        MOD = 10 ** 9 + 7
        
        def find(n):
            if n in dp:
                return dp[n]
            
            dp[n] = (find(n-1) * (2*n-1) * n ) % MOD
            return dp[n]
        
        return find(n)
        