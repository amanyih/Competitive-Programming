class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cache = {}
        def search(index,level,prev):
            if (index,level) in cache:
                return cache[(index,level)]
            if level == 0:
                return 1
            if index < 0 :
                return 0
            
            count = 0
            for i in range(index):
                if rating[i] > prev:
                    count += search(i,level -1 ,rating[i])
            cache[(index,level)] = count
            return count
        
        forward = search(len(rating),3,-inf)
        rating = rating[::-1]
        cache = {}
        reverse = search(len(rating),3,-inf)
        return reverse  + forward
            
            
                
                
            
            
            
            
            
        
        
        
        
                
            
            
                
                
            
        