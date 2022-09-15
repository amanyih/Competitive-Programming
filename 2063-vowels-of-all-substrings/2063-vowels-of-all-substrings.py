class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {"a","e","i","o","u"}
        wordsBefore = 0
        ans = 0
        for i in range(len(word)):
            if word[i] in vowels:
                wordsAfter = len(word) - i
                totalWords = wordsAfter + wordsAfter*wordsBefore
            
                ans += totalWords
            wordsBefore += 1
        
        
        return ans
        