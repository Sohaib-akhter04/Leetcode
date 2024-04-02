'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_Profit=0
        min_price=prices[0]
        for i in range(len(prices)):
            max_Profit=max(max_Profit,prices[i]-min_price)
            min_price=min(min_price,prices[i])
        return max_Profit