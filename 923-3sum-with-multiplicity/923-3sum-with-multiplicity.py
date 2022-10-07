class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        
        
        ans = 0
        
        for i in range(len(arr)):
            
            newTarget = target - arr[i]
            left = i +1
            right =  len(arr) - 1
            
            while left < right:
                
                if arr[left] + arr [right] < newTarget:
                    left += 1
                elif arr[left] + arr[right] > newTarget:
                    right -= 1
                elif arr[left] != arr[right]:
                    left_c = 0
                    right_c = 0
                    l = left
                    r = right
                    while arr[l] == arr[left]:
                        left_c += 1
                        l += 1
                    while arr[right] == arr[r]:
                        right_c += 1
                        r -= 1
                    ans += (left_c * right_c)
                    left = l
                    right = r
                else:
                    ans += (right-left+1) * (right-left) //2
                    break
            
        return ans % (10**9+7)
                    
            
            
            
                    
                    
                
                
            