class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        strings ={}
        
        def findString(n):
            if n in strings:
                return strings[n]
            
            if n == 1:
                return "0"
            else:
                sn = findString(n-1)
                sn = sn + "1" + reverse(invert(sn))
                
                strings[n] = sn
            return sn
        def reverse(word):
            neww = ""
            for i in range(len(word)-1,-1,-1):
                neww+= word[i]
            return neww
        def invert(word):
            neww = ""
            for char in word:
                if char =="0":
                    neww+="1"
                else:
                    neww+="0"
            return neww
        
        return findString(n)[k-1]
            
            
        
        