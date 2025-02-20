class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        dp = [0] * len(prices)
        min_price = prices[0]
        dp[0] = 0

        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)

            profit = prices[i] - min_price

            if profit > dp[i-1]:
                dp[i] = profit
            else:
                dp[i] = dp[i-1]
        
        return dp[len(prices) - 1]
