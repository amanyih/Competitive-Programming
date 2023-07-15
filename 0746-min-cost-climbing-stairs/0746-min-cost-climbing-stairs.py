class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        store = [cost[-1],cost[-2]]
        
        for i in range(len(cost)-3,-1,-1):
            cur = min(store[-1],store[-2]) + cost[i]
            store.append(cur)
        
        # print(store)
        return min(store[-1],store[-2])
        
        
        
