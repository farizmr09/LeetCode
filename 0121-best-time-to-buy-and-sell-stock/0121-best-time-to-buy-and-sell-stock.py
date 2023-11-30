class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = 999999999
        max_sell = 0
        for i in range(0, len(prices)):
            min_buy = min(min_buy, prices[i])
            max_sell = max(max_sell, prices[i] - min_buy)
        return(max_sell)