class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxProfit = 0
        minBuy = prices[0]

        for price in prices:
            minBuy = min(price, minBuy)
            maxProfit = max(price - minBuy, maxProfit)

        return maxProfit
