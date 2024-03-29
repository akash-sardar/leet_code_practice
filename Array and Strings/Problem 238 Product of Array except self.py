class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        rev_nums = nums[::-1]
        prefix = list()
        postfix = list()
        hold_product = 1
        hold_product_rev = 1
        for i in range(n):
            prefix.append(nums[i] * hold_product)
            postfix.append(rev_nums[i] * hold_product_rev)
            hold_product = nums[i] * hold_product
            hold_product_rev = rev_nums[i] * hold_product_rev
        postfix.reverse()

        out = list()
        for i in range(n):
            if i == 0:
                out.append(1 * postfix[i+1])
            elif i == n-1:
                out.append(prefix[i-1] * 1)
            else:
                out.append(prefix[i-1] * postfix[i+1])
        return out


sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
#print(sol.canJump([1,1,0,1]))
#print(sol.canJump([1,1,2,2,0,1,1]))
#print(sol.canJump([3,2,1,0,4]))
#print(sol.canJump([2,3,1,1,4]))
#print(sol.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))
