class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        spent = prices[0] + prices[1]
        if spent > money:
            return money
        else:
            return money - spent