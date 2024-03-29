class Solution:
    def removeDuplicates(self, nums) -> int:
        hold = -101
        num = nums.copy()
        for i in num:
            print('i',i)
            if i == hold:
                print('hold', hold)
                hold = i
                nums.remove(i)
                print(nums)
            else:
                hold = i
        return len(nums)

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

