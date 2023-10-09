class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        winLen = len(needle)
        MOD = 10 ** 9 + 7

        powers = {i : 27**i for i in range(winLen)}
        needlehash = 0
        for i,char in enumerate(needle):
            cur = ord(char) - ord("a") + 1
            needlehash += cur * powers[winLen-1-i]
        
        curSum = 0
        left = 0
        
        for right in range(len(haystack)):
            char = haystack[right]
            curSum = curSum * 27 + (ord(char)-ord("a")+1)
            
            if curSum == needlehash:
                return left
            if right - left + 1 == winLen:
                left_char = haystack[left]
                curSum -= (ord(left_char)-ord("a")+1) * powers[winLen-1]
                left += 1
        return -1
            

        

