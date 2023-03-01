class Solution:
    def reverseString(self, s: List[str],left = 0) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        right = len(s)-1 - left
        
        if left >= right:
            return
        s[left],s[right] = s[right],s[left]
        left += 1
        
        self.reverseString(s,left)

        
        
        