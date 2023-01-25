class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        
        ans = [-1] * n
        curMax = -1
        
        
        for i in range(n-1,-1,-1):
            ans[i] = curMax
            curMax = max(curMax,arr[i])
        return ans
            
        