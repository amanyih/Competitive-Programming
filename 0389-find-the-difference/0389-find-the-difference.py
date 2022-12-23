class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
        count_s = {}
        count_t = {}
        
        for c in s:
            count_s[c] = count_s.get(c,0) + 1
        for c in t:
            count_t[c] = count_t.get(c,0) + 1
        
        for key in count_t:
            if count_t[key] - count_s.get(key,0) > 0:
                return key
        
        
        
        
        