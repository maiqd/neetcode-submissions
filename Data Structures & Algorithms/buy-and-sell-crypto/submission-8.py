class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        res = 0
        for price in prices:
            minBuy = min(price, minBuy)
            res = max(res, price - minBuy)
        return res