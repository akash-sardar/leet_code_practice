class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cp = prices[0]
        m = len(prices)
        profit = 0
        total_profit = 0
        for i in range(1,m):
            cp = prices[i-1]
            #print('cp', cp)
            if prices[i] > cp:
                profit = prices[i] - cp
                #print('price', prices[i])
                #print('Profit', profit)
            else:
                profit = 0
            total_profit = total_profit + profit
            #print('tp', total_profit)
        return total_profit

sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))
