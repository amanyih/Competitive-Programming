class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def count(n):
            if n in memo:
                return memo[n]

            if n <= 1:
                return cost[n]

            memo[n] = min(count(n - 1), count(n - 2)) + cost[n]
            return memo[n]

        return min(count(len(cost) - 1), count(len(cost) - 2))
