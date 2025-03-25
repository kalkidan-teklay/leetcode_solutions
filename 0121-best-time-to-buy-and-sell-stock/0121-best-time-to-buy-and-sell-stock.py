class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        selling = prices[0]  
        buying = prices[0]
        profit = 0
        max_profit = profit
        for i in range(len(prices)):  
            if buying > prices[i]:
                buying = prices[i]
                selling = prices[i]
            if selling < prices[i]:
                selling = prices[i]
                profit = selling-buying
                max_profit = max(profit, max_profit)
        return max_profit
        