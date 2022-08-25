class Solution:
    def removeKdigits(self, num, k) -> str:
        stack =[]
        count = 0

        for n in num:
            while count < k and stack and stack[-1] > n:
                count += 1
                stack.pop()
            
            stack.append(n)
        
        ans = "".join(stack[:len(stack)-k+count] )
        if len(ans) == 0: ans = "0"

        return str(int(ans))


