from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_time = prices[0]
        for price in prices[1:]:
            max_profit = max(max_profit, price - buy_time)
            buy_time = min(buy_time, price)

        return max_profit