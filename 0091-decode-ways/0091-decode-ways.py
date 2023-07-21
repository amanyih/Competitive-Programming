class Solution:
    def numDecodings(self, s: str) -> int:
    
        cache = {len(s):1}
        
        def backtrack(i):
            if i in cache:
                return cache[i]
            
            if s[i] == "0":
                return 0
            
            res = backtrack(i+1)
            
            if (i+1) < len(s) and (s[i]=="1" or (s[i] == "2" and s[i+1] not in "789")):
                res += backtrack(i+2)
            
            cache[i] = res
            
            return res
        
        return backtrack(0)
            
            
        