class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        
        
        def helper(n,k):
            if k == 1:
                return 0 
            
            if k%2:
                return helper(n-1,ceil(k/2))
            else:
                return 1- helper(n-1,ceil(k/2))
        return helper(n,k)
                
            
        