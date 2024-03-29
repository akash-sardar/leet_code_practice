class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 1
        nums.reverse()
        if len(nums) == 1:
            return True
        while nums:
            if nums[i] >= i:
                nums = nums[i:]
                if len(nums) > 1:
                    i = 1
                else:
                    nums.pop()
            else:
                i = i + 1
                if i == len(nums):
                    break
        if nums:
            return False
        else:
            return True


sol = Solution()
print(sol.canJump([2,0]))
#print(sol.canJump([1,1,0,1]))
#print(sol.canJump([1,1,2,2,0,1,1]))
#print(sol.canJump([3,2,1,0,4]))
#print(sol.canJump([2,3,1,1,4]))
#print(sol.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))
