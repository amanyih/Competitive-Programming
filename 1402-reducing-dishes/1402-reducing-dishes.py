class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        cache = {}
        
        def find(index,order):
            if (index,order) in cache:
                return cache[(index,order)]
            if index < 0:
                return 0
            
            jump = find(index-1,order)
            cook = satisfaction[index] * order + find(index-1,order+1)
            
            cur = max(jump,cook)
            cache[(index,order)] = cur
            return cur
        return find(len(satisfaction)-1,1)
            
            
            
        
        