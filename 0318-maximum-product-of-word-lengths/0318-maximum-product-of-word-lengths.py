class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        
        def countBit(num):
            count = 0
            mask = 1
            shift = 0

            while mask <= num:
                if mask & num !=0:
                    count += 1
                shift += 1
                mask = 1<<shift
            return count
        def toNum(string):
            number = 0
            for char in string:
                i = ord(char) - 97
                number |= 1 << i
            return number
        numbers = [[toNum(word),countBit(toNum(word))] for word in words]
        ans = 0
        for i in range(len(words)):
            ni,nc = numbers[i]
            for j in range(i+1,len(words)):
                ji,jc= numbers[j]
                if nc + jc == countBit(ji | ni):
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans
                
                
                