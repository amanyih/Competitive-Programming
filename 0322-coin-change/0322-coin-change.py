class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [inf] * (amount + 1)
        cache[0] = 0
        
        for i in range(1,amount + 1):
            for coin in coins:
                
                if i - coin >=0:
                    cache[i] = min(cache[i],1+cache[i-coin])
        
        if cache[amount] != inf:
            return cache[amount]
        return -1
        
        
        