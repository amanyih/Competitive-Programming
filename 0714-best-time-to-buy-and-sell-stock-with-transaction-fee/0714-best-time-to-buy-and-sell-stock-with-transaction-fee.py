class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        stock, not_stock = [0] * n, [0] * n

        stock[0] = -prices[0]

        for i in range(1, n):
            stock[i] = max(stock[i - 1], not_stock[i - 1] - prices[i])
            not_stock[i] = max(not_stock[i - 1], stock[i - 1] + prices[i] - fee)

        return not_stock[-1]
