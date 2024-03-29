class Solution(object):
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        if k == 0 or l == 1:
            return nums
        else:
            for i in range(k):
                nums.insert(0, nums[-1])
                nums.pop()
        return nums



sol = Solution()
print(sol.rotate(nums = [1,2,3,4,5,6,7], k = 3))
