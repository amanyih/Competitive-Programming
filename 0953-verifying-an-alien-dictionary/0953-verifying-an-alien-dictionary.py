class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        value = defaultdict(int)
        value[0] = -1
        for i,char in enumerate(order):
            value[char] = i
        
        def compare(word1,word2):
            n = max(len(word1),len(word2))
            
            for i in range(n):
                c1 = word1[i] if i < len(word1) else 0
                c2 = word2[i] if i <  len(word2) else 0
                val1 = value[c1]
                val2 =  value[c2]
                if val1 < val2:
                    return True
                elif val1 > val2:
                    return False
            return True
        
        
        for i in range(1,len(words)):
            if not compare(words[i-1],words[i]):
                print(words[i])
                return False
        return True