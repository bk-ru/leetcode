class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        current = float('inf')
        for i in prices:
            if (i - current > profit):
                profit = i - current
            if (i < current):
                current = i
        return profit