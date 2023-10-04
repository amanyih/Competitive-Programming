class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        lst = []
        for i,cost in enumerate(costs):
            a,b = cost
            lst.append((a-b,i))
            
        lst.sort(key = lambda x : x[0])
        
        ans = 0
        for i in range(n):
            if i < n//2:
                ans += costs[lst[i][1]][0]
            else:
                ans += costs[lst[i][1]][1]
        
        return ans
        