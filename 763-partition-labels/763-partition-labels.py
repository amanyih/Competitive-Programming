class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        a   b   a   c   c   b   d   e   f   f   e   d
        0   1   2   3   4   5   6   7   8   9   10  11
        
        """
        last = {}
        for i,char in enumerate(s):
            last[char] = i
        
        left = 0
        right = 0
        ans = []
        
        
        for index in range(len(s)):
            
            right = max(right,last[s[index]])
            
            if index == right:
                
                ans.append(right - left + 1)
                left = index + 1
        
        
        return ans
            
                    
            
        