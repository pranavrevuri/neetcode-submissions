class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = prices[0]
        best_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < cheapest_price:
                cheapest_price = prices[i]
            profit = prices[i] - cheapest_price
            if profit > best_profit:
                best_profit = profit
        
        return best_profit