class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        
        def freqLexS(string):
            
            count = [0] * 26
            minChar = 27
            
            for char in string:
                count[ord(char)-97] += 1
                minChar = min(minChar,ord(char)-97)
            # print(string,count[minChar])
            return count[minChar]
        wordsFreq = []
        
        def findPosition(string):
            target = freqLexS(string)
            idx = bisect_left(wordsFreq,target+1)
            if idx >= len(words):
                return 0
            if idx == 0 and wordsFreq[idx] > target:
                return len(words)
            
            return len(words) - idx
                
        
        
        for word in words:
            wordsFreq.append(freqLexS(word))
        wordsFreq.sort()
        
        res = []
        
        for query in queries:
            res.append(findPosition(query))
        
        return res
        
        
        
                
            