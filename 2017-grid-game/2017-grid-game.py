class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        firstPrefix  =  list(accumulate(grid[0]))
        secondPrefix = list(accumulate(grid[1]))
        n = len(grid[0])
        
#         def getSum(arr,left,right):
#             return (arr[right] if right >= 0 else arr[0]) - (arr[left-1] if left > 0 else 0)
        
        maxPoints = inf
        
        for i in range(n):
            
            curPoints = max(firstPrefix[-1]-firstPrefix[i],secondPrefix[i-1] if i > 0 else 0)
            maxPoints = min(curPoints,maxPoints)
        return maxPoints
#         for i in range(n):
#             if i<turnPoint:
#                 cur = getSum(secondPrefix,0,i)
#                 maxP = max(maxP,cur)
#             elif i > turnPoint:
#                 cur = getSum(firstPrefix,i,n-1)
#                 # print("i",i)
#                 # print(cur,i,n-1,firstPrefix)
#                 maxP = max(maxP,cur)
#         return maxP
            
            
            
        
        
        
        
        