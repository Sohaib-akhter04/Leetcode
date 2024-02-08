#28. Find the Index of the First Occurrence in a String


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

if __name__=="__main__":
    prices=[7,6,4,3,1]
    solution=Solution()
    temp=solution.maxProfit(prices)
    print(temp)
   