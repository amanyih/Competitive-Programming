class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        ans = 0
        
        stack = []
        st = set()
        
        for i,char in enumerate(s):
            
            if char == "(":
                stack.append(i)
            else:
                index = stack.pop()
                cur = 0
                if index not in st:
                    cur += 1
                pointer = len(stack) - 1
                while pointer >=0:
                    cur *= 2
                    st.add(stack[pointer])
                    pointer -=1
                ans += cur
        return ans