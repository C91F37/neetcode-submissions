class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = 101
        max_profit = -1
        for i in prices:
            min_so_far = min(min_so_far, i)
            max_profit = max(max_profit, i-min_so_far)
        return max_profit