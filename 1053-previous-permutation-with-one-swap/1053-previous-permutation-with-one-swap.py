class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        def get_miss_placed(arr):
            
            for i in range(len(arr)-2,-1,-1):
                if arr[i] > arr[i+1]:
                    return i
            return len(arr) - 1
                
                
        
        def maxAfter(arr,inp):
            if inp == len(arr) - 1: return inp
            cur = inp + 1
            
            for i in range(inp + 1, len(arr)):
                if arr[i] > arr[cur] and arr[i] < arr[inp]:
                    cur = i
            return cur
        i = get_miss_placed(arr)
        j = maxAfter(arr,i)
        arr[i],arr[j] = arr[j],arr[i]
        return arr
        
        
        
        