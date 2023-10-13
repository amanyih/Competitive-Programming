class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        cur = 0
        total = 0
        ans = 0
        
        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]
            cur += g-c
            total += g-c
            if cur < 0 :
                cur = 0
                ans = i +1
        if total < 0:
            return -1
        return ans
        