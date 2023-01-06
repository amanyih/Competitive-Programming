class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        for i in range(len(costs)):
            
            if coins - costs[i] >= 0 :
                coins -= costs[i]
            else:
                return i
        
        return i + 1