class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count = {}
        
        for char in t:
            count[char] = 1 + count.get(char,0)
        
        left = 0
        curCount = {}
        
        ansLst = []
        minLength = len(s) + 1
        def isT(curCount):
            
            for key in count:
                if (key not in curCount) or (key in curCount and curCount[key] < count[key]):
                    return False
            return True
        
        for right in range(len(s)):
            if s[right] in count:
                curCount[s[right]] = 1 + curCount.get(s[right],0)
                
            while isT(curCount):
                
                if right - left + 1 < minLength:
                    if len(ansLst) >0:
                        ansLst[0] = left
                        ansLst[1] = right
                    else:
                        ansLst.append(left)
                        ansLst.append(right)
                    minLength = right - left + 1
                if s[left] in curCount:
                    curCount[s[left]] -= 1
                left += 1
        print(curCount)
        
        return "" if len(ansLst) == 0 else s[ansLst[0]:ansLst[1]+1]
        
        