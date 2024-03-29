class Solution:
    def removeDuplicates(self, nums) -> int:
        m = len(nums)
        count = 0
        i = 0
        k = 0
        while i < m:
            if i == 0:
                count = count + 1
                i = i + 1
                k = k + 1
                continue
            if nums[i] == '_':
                break
            if nums[i] == nums[i-1]:
                count = count + 1
                k = k + 1
                if count > 2:
                    nums.pop(i)
                    nums.append('_')
                    i = i-1
                    k = k - 1
            else:
                count = 1
                k = k + 1
            i = i + 1
        return k


sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))
