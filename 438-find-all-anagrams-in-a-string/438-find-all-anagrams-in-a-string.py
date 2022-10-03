class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        count = {} # {a:1,b:1,c:1}
        for char in p:
            count[char] = count.get(char,0) + 1
        
        left = 0
        curCount = {}
        
        def isAnagram(count,curCount):
            if len(count) != len(curCount):
                return False
            for char in count:
                if char not in curCount or(count.get(char) != curCount.get(char,0)):
                    return False
            return True
        
        ans =[]
        
        for right in range(len(s)):
            curCount[s[right]] = curCount.get(s[right],0) + 1
            
            if isAnagram(count,curCount):
                ans.append(left)
            
            if right - left + 1 > len(p)- 1:
                curCount[s[left]] = curCount.get(s[left]) - 1
                if curCount[s[left]] == 0:
                    del curCount[s[left]]
                left += 1
        
        return ans
                
                
                
        
            
        
        
        
                