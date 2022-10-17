class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        chars = "abcdefghijklmnopqrstuvwxyz"
        ans = []
        
        def camel(query,pattern):
            p = 0
            
            for q in range(len(query)):
                if p < len(pattern):
                    if query[q] == pattern[p]:
                        p += 1
                    elif query[q] in chars.upper():
                        return False
                else:
                    if query[q] in chars.upper():
                        return False
            return True if p >= len(pattern) else False
                
        """
        ["ForceFeedBack"]
               l
        FB
         i
        """
        
        
        for query in queries:
            ans.append(camel(query,pattern))
        return ans
            
        
        