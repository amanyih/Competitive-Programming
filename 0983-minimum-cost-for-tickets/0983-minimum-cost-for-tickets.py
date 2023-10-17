class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        cache = {}
        
        
        def calculate(index,prev,p_amount):
            
            if (index,prev,p_amount) in cache:
                return cache[(index,prev,p_amount)]
            
            if index < 0:
                return 0
            total = 0
            total += min(
              costs[0] +  calculate(index-1,1,days[index]),
              costs[1] +  calculate(index-1,7,days[index]),
              costs[2] +  calculate(index-1,30,days[index]))
            if prev != 1 and p_amount - days[index] < prev:
                total = min(total,calculate(index-1,prev,p_amount))
            
            cache[(index,prev,p_amount)] = total
            
            return total
        
        return calculate(len(days)-1,1,0)
                
                