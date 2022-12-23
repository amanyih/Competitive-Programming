class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        loop_count = 1
        
        left = 0
        right = 0
        res = ""
        
        while left < len(word1) and right < len(word2):
            if loop_count % 2:
                res += word1[left]
                left += 1
            else:
                res += word2[right]
                right += 1
            loop_count += 1
        
        if left < len(word1):
            res += word1[left:]
        elif right < len(word2):
            res += word2[right:]
        return res
            