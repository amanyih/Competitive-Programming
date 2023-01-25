class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        
        curMax = -1
        
        
        for i in range(n-1,-1,-1):
            curNum = arr[i]
            arr[i] = curMax
            curMax = max(curMax,curNum)
        return arr
            
        