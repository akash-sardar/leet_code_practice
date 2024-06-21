class Solution(object):
    def minSubArrayLen(self, target, nums):
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total  = total + nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total = total - nums[l]
                l = l + 1
        
        return 0 if res == float("inf") else res



            


sol = Solution()
#print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
#print(sol.minSubArrayLen(target = 11, nums = [1,2,3,4,5]))
#print(sol.minSubArrayLen(target = 213, nums = [12,28,83,4,25,26,25,2,25,25,25,12]))
print(sol.minSubArrayLen(target = 80, nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]))
