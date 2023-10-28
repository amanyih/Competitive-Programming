class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        graph = {
            "a" : {"e"},
            "e":{"a","i"},
            "i" : {"a","e","o","u"},
            "o": {"i","u"},
            "u":{"a"}}
        cache = {}
        
        def dp(cur,prev):
            if (cur,prev) in cache:
                return cache[(cur,prev)]
            
            if cur == n:
                return 1
            count = 0
            for char in graph[prev]:
                count += dp(cur+1,char)
            cache[(cur,prev)] = count
            return count
        ans = 0
        for key in graph:
            ans += dp(1,key)

        return ans % MOD