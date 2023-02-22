class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        left = 0
        k = len(p)
        ans = []
        def checkDict(count):
            for key in count:
                if count[key] != 0:
                    return False
            return True
        
        for right in range(len(s)):
            if s[right] in pCount:
                pCount[s[right]] -= 1
            if right - left + 1 == k:
                if checkDict(pCount):
                    ans.append(left)
            
                if s[left] in pCount:
                    pCount[s[left]] += 1
                left += 1
                
                
            
        
        return ans
             
        