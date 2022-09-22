class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        stack = []
        
        for char in s:
            if char != " ":
                stack.append(char)
            else:
                while stack:
                    ans += stack.pop()
                ans += " "
        
        while stack:
            ans+= stack.pop()
            
        return ans
        