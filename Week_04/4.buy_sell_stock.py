class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        index = 1
        while index < len(prices):
            if prices[index] > prices[index - 1]:
                profit += prices[index] - prices[index - 1]
            index += 1
        return profit
