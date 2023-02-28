class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        winSize = len(s1)
        count = {}
        for char in s1:
            count[char] = count.get(char,0) + 1
        
        curCount = {}
        
        left = 0
        for right in range(len(s2)):
            curCount[s2[right]] = curCount.get(s2[right],0) + 1
            
            if right - left + 1 == winSize:
                if curCount == count:
                    return True
                
                curCount[s2[left]] -= 1
                if curCount[s2[left]] == 0:
                    del curCount[s2[left]]
                left += 1
        return False