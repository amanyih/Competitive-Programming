class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = [i for i in range(1,n + 1)]
        
        left = 0
        
        while left != len(lst)-1:
            if (left + 1) % k != 0:
                lst.append(lst[left])
            
            left += 1
        
        return lst[left]
    
                    
                    
            
            
            
            