class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_value = max(citations)
        h_index = 0
        while h_value > 0:
            counter = 0
            for i in range(len(citations)):
                if citations[i] >= h_value:
                    counter = counter + 1
                    if counter >= h_value:
                        if h_index < h_value:
                            h_index = h_value
            h_value = h_value - 1

        return h_index

sol = Solution()
#print(sol.hIndex([11,15]))
print(sol.hIndex([3,0,6,1,5]))
#print(sol.canJump([1,1,0,1]))
#print(sol.canJump([1,1,2,2,0,1,1]))
#print(sol.canJump([3,2,1,0,4]))
#print(sol.canJump([2,3,1,1,4]))
#print(sol.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))
