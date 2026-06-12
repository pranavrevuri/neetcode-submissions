class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left_buy = 0
        right_sell = 1
        
        while (right_sell < len(prices)):
            if prices[right_sell] < prices[left_buy]:
                left_buy = right_sell
            profit = prices[right_sell] - prices[left_buy]
            if profit > max_profit:
                max_profit = profit
            right_sell += 1
        
        return max_profit