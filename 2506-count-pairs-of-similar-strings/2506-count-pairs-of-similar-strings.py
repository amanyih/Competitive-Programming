class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        wordsSet = []
        for word in words:
            s = set()
            for c in word:
                s.add(c)
            wordsSet.append(s)
        
        ans= 0
        for i in range(len(wordsSet)):
            for j in range(i+1,len(wordsSet)):
                if wordsSet[i] == wordsSet[j]:
                    ans += 1
        
        return ans
            
        