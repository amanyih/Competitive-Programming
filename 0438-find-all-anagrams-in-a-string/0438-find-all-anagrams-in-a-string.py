class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        pCount = Counter(p)
        cur = {}
        ans = []
        
        for right in range(len(s)):
            cur[s[right]] = cur.get(s[right],0) +1
            
            if right - left + 1 == len(p):
                if cur == pCount:
                    ans.append(left)
                cur[s[left]] -= 1
                if cur[s[left]] == 0:
                    del cur[s[left]]
                left += 1
        
        return ans
             
        