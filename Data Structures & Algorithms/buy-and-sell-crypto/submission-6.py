class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        minPrice = prices[0]
        for i in range(1, len(prices), 1):
            minPrice = min(prices[i], minPrice)
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit