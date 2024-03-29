class Solution:
    def removeElement(self, nums, val: int) -> int:
        li = nums.copy()
        for i in li:
            if i == val:
                nums.remove(i)
        return len(nums)

sol = Solution()
print(sol.removeElement([3,2,2,3], 3))

