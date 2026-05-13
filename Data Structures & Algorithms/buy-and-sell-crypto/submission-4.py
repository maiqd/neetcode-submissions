class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for buyIndex in range(len(prices)):
            sellIndex = buyIndex + 1
            while sellIndex < len(prices):
                profit = prices[sellIndex] - prices[buyIndex]
                maxProfit = max(profit, maxProfit)
                sellIndex+=1

        return maxProfit