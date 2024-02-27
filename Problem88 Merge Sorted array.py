class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # print(nums1)
        # print(nums2)
        for i in range(n):
            for j in range(len(nums1)):
                if nums1[j] > nums2[i]:
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    break
            if j == len(nums1)-1:
                if nums1[j] == 0:
                    nums1[-(n-i)] = nums2[i]
                else:
                    nums1.append(nums2[i])
        return nums1

sol = Solution()
print(sol.merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2] , n = 3))
#print(sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

# digits = [1,2,4, 4, 5, 6]
# for i in range(len(digits)-1, 0, -1):
#     print(i)
