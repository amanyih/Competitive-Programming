class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        MOD = (10**9) + 7
        n = len(arr)

        
        def calSum(left,cur,right):
            return ((cur-left) * (right - cur)) * arr[cur]
        
        stack = []
        ans = 0
        
        for i,num in enumerate(arr):
            
            while stack and arr[stack[-1]] >= num:
                cur = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                
                ans += calSum(left,cur,right)
            stack.append(i)
        while stack:
            cur = stack.pop()
            left = stack[-1] if stack else -1
            right = n
            ans += calSum(left,cur,right)
        
        return ans % MOD
        
                
                
        