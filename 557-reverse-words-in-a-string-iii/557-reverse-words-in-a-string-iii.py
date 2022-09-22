class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        
        for i in range(len(lst)):
            newWord = ""
            for j in range(len(lst[i]) -1,-1,-1):
                newWord += lst[i][j]
            
            lst[i] = newWord
        
        return " ".join(lst)
        