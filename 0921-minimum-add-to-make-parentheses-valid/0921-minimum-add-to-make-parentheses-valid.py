class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        ans = 0
        
        for char in s:
            if char == "(":
                stack.append(char)
            elif stack:
                stack.pop()
            else:
                ans += 1
        
        return ans + len(stack)
        