class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        val = len(arr)
        
        ans = []
        
        while val > 0:
            
            index = arr.index(val)
            
            if index != val -1:
                if index != 0:
                    ans.append(index + 1)
                    self.flip(arr,index + 1)
                
                ans.append(val)
                self.flip(arr,val)
            
            
            val -=1
        
        return ans
    
    
    
    def flip(self,arr,k):
        
        i = 0
        while i < k:
            arr[i],arr[k-1] = arr[k-1],arr[i]
            i+=1
            k-=1