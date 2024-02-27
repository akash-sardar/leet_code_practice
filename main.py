class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum_of_gas = sum(gas)
        sum_of_cost = sum(cost)
        diff = []
        pos_index = []
        if sum_of_gas < sum_of_cost:
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start







sol = Solution()
#print(sol.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
#print(sol.canCompleteCircuit([2,3,4], cost = [3,4,3]))
print(sol.canCompleteCircuit([5,1,2,3,4], cost = [4,4,1,5,1]))
