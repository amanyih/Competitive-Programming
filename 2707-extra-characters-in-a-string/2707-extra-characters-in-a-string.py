class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        words = set(dictionary)
        
        @cache
        def search(i):
            
            if i == len(s):
                return 0
            
            ans = 1 + search(i+1)
            
            for j in range(i,len(s)):
                if s[i:j+1] in words:
                    ans = min(ans,search(j+1))
            
            return ans
        
        return search(0)
        