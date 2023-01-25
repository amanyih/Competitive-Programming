class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        maxInd = 0
        
        for i in range(len(arr)):
            if arr[i] > arr[maxInd]:
                maxInd = i
        
        if maxInd == len(arr) - 1 or maxInd == 0:
            return False
        
        for i in range(1,maxInd):
            if arr[i] <= arr[i-1]:
                return False
        for i in range(maxInd+1,len(arr)):
            if arr[i] >= arr[i-1]:
                return False
        
        return True
            
            
        