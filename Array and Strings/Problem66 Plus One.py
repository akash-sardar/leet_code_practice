class Solution:
    def plusOne(self, digits):
        carry = 0
        sum = digits[-1] + 1
        if sum > 9:
            digits[-1] = 10-sum
            carry = 1
            if len(digits)==1:
                digits.insert(0, carry)
                return digits
            for i in range(len(digits)-2, -1, -1):
                if carry == 1:
                    sum = digits[i] + carry
                    if sum > 9:
                        carry = 1
                        digits[i] = 10 -sum
                        if i == 0:
                            digits.insert(0, carry)
                    else:
                        digits[i] = sum
                        carry = 0
        else:
            digits[-1] = sum
        return digits


sol = Solution()
print(sol.plusOne([9,9,9,9]))

# digits = [1,2,4, 4, 5, 6]
# for i in range(len(digits)-1, 0, -1):
#     print(i)
