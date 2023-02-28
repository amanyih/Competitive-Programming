class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        prefix = [0] * (len(s) +1)
        for shift in shifts:
            i,j,d = shift
            if d:
                prefix[i] += 1
                if j+1 < len(s):
                    prefix[j+1] -= 1
            else:
                prefix[i] -= 1
                if j +1 < len(s):
                    prefix[j+1] += 1
        
        
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1] + prefix[i]
        
        letters = []
        
        for i,char in enumerate(s):
            curOrd = ord(char) - 97
            newOrd = (curOrd + prefix[i]) % 26 + 97
            letters.append(chr(newOrd))
        
        return "".join(letters)
            
            