class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            r += 1
        return max_profit
