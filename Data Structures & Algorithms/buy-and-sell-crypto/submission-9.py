class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]
        for price in prices:
            minPrice = min(price, minPrice)
            profit = price - minPrice
            res = max(res, profit)
        return res