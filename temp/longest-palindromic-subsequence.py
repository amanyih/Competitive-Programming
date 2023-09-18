class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        
        cache = [[0 for i in range(n)] for i in range(n)]
        
        for i in range(n):
            cache[i][i] = 1
        
        for i in range(2,n+1):
            for j in range(n-i+1):
                last = j + i - 1
                
                if s[j] == s[last]:
                    # print("j",j,"last",last,"i",i)
                    cache[j][last] = cache[j+1][last-1] + 2
                else:
                    cache[j][last] = max(cache[j+1][last],cache[j][last-1])
        
        return cache[0][n-1]
                
            
        