class Solution(object):
    def maxProfit(self, prices):
        cp = prices[0]
        max_profit = 0
        for price in prices:
            if price < cp:
                cp = price
            elif max_profit < price - cp:
                max_profit = price - cp
        return max_profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
