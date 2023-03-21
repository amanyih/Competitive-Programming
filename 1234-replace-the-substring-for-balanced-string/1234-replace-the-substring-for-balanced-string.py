class Solution:
    def balancedString(self, s: str) -> int:
        
        count = Counter(s)
        c = len(s) // 4
        st = set()
        
        for key,value in count.items():
            st.add(value)
        if len(st) == 1 and len(count) == 4:
            return 0
        
        left = 0
        ans = inf
        cur = {}
        
        def isValid(win,c):
            for key,value in count.items():
                out = count[key] - win.get(key,0)
                if out > c:
                    return False
            return True
        for right,char in enumerate(s):
            cur[char] = cur.get(char,0) + 1
            
            while isValid(cur,c) and left <= right:
                ans = min(right-left+1,ans)
                
                cur[s[left]] -= 1
                
                if cur[s[left]] == 0:
                    del cur[s[left]]
                
                left += 1
        return ans
            
        
        
        