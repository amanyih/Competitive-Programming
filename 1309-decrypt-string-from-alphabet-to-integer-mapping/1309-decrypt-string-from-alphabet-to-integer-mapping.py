class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        storeage = []
        
        right = len(s) - 1
        
        while right >= 0:
            
            if s[right].isalnum():
                storeage.append(chr(int(s[right])+96))
                right -= 1
            else:
                storeage.append(chr(int(s[right-2:right])+96))
                right -= 3
        storeage.reverse()       
        return "".join(storeage)
                
                
        