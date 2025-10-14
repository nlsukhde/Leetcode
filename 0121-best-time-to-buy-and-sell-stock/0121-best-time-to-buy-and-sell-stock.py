class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = 0
        maxProfit = 0

        for i in range(len(prices)):
            if i == 0:
                lowest = prices[i]
            
            lowest = min(lowest, prices[i])

            curProfit = prices[i] - lowest

            maxProfit = max(maxProfit,curProfit)
        
        return maxProfit
        