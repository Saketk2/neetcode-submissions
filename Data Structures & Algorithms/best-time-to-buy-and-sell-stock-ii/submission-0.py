class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gains = []
        for i in range(1, len(prices)):
            gains.append(prices[i] - prices[i - 1])
        profit = 0
        for g in gains:
            if g > 0:
                profit += g
        return profit

    
        