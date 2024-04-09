class Solution:
    def twoSum(self, numbers, target):
        '''
         Amazon: 167. Two Sum II - Input Array Is Sorted
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
        The tests are generated such that there is exactly one solution. You may not use the same element twice.
        Your solution must use only constant extra space.
        '''
        # Brute Force - Solution n2
        # hold_i =0
        # while numbers:
        #     for i, value_i in enumerate(numbers):
        #         for j, value_j  in enumerate(numbers[i+1:]):
        #             if value_i + value_j == target:
        #                 return (hold_i+1, hold_i+j+2)
        #             elif value_i + value_j > target:
        #                 numbers = numbers[:i+j+1]
        #                 break
        #         hold_i = hold_i + 1
        #         numbers = numbers[i+1:]
        #         break
        pointer_1 = 0
        pointer_2 = len(numbers) - 1
        while numbers[pointer_1:pointer_2]:
            if numbers[pointer_1] + numbers[pointer_2] > target:
                pointer_2 = pointer_2 - 1
            elif numbers[pointer_1] + numbers[pointer_2] < target:
                pointer_1 = pointer_1 + 1
            else:
                return (pointer_1 + 1, pointer_2 + 1)


sol = Solution()
#print(sol.convert(s="PAYPALISHIRING", numRows = 3))
print(sol.twoSum([5,25,75], 100))
