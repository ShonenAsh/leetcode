class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        profit = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r

            profit = max(profit, prices[r] - prices[l])

        return profit
