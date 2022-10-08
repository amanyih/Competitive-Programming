class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        ans = 0
        right = 0
        
        
        
        while right < len(arr):
            
            left = right
            
            if right + 1 < len(arr) and arr[right] < arr[right+1]:
                
                while right + 1 < len(arr) and arr[right] < arr[right+1]:
                    right += 1
                    
                if right + 1 < len(arr) and arr[right] > arr[right+1]:
                    while right + 1 < len(arr) and arr[right] > arr[right+1]:
                        right += 1

                    ans = max(ans,right-left+1)
            else:
                right += 1
        
        return ans
        
        
        
        
        