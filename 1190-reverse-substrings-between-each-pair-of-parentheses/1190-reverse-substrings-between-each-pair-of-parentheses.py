class Solution:
    def reverseParentheses(self, s: str) -> str:
        sLst =[i for i in s]
        stack = []
        ans = ""

        for i in range(len(s)):
            if sLst[i] == "(":
                stack.append(i)
            elif sLst[i] == ")":
                left = stack[-1]
                right = i
                while left < right:
                    sLst[left],sLst[right] = sLst[right],sLst[left]
                    left += 1
                    right -=1
                stack.pop()
        
        for char in sLst:
            if char != "(" and char != ")":
                ans += char
        
        return ans