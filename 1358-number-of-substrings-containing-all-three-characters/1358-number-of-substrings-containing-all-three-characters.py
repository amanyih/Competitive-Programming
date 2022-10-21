class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        three = {"a":1,"b":1,"c":1}
        
        def check(cur):
            
            for key in three:
                if (key not in cur) or (key in cur and cur[key] < three[key]):
                    return False
            
            return True
        
        left = 0
        cur = {}
        ans = 0
        
        for right,char in enumerate(s):
            
            cur[char] = 1 + cur.get(char,0)
            
            while check(cur):
                
                ans += len(s) - right
                cur[s[left]] -= 1
                left += 1
        
        return ans
                
            
        