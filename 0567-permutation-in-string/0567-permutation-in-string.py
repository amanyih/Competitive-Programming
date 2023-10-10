class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        winSize = len(s1)
        countS1 = {}
        
        for i in range(len(s1)):
            countS1[s1[i]] = countS1.get(s1[i],0) + 1
        
        left = 0
        cur = {}
        for right in range(len(s2)):
            cur[s2[right]] = cur.get(s2[right],0) + 1
            
            if cur == countS1:
                return True
            if right - left + 1 == winSize:
                cur[s2[left]] -= 1
                if cur[s2[left]] == 0:
                    del cur[s2[left]]
                
                left += 1
        return False