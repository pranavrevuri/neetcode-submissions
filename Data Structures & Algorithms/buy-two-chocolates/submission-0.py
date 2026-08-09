class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        cheapest = prices[0] + prices[1]

        if cheapest > money:
            return money
        else:
            return money - cheapest