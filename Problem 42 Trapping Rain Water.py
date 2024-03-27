class Solution:
    def trap(self, height) -> int:
        accum = list()
        max_left = list()
        max_right = list()
        hold = 0
        for i, value in enumerate(height):
            max_left.append(hold)
            if value >= hold:
                hold = value
        height = height[::-1]
        hold = 0
        for i, value in enumerate(height):
            max_right.append(hold)
            if value >= hold:
                hold = value
        height = height[::-1]  
        max_right = max_right[::-1]
        min_value = list()
        for i, value in enumerate(max_left):
            if value == 0 or max_right[i] == 0:
                min_value.append(0)
            elif value < max_right[i]:
                min_value.append(value)
            else:
                min_value.append(max_right[i])
        # print(height)
        # print(max_left)
        # print(max_right)
        # print(min_value)
        for i, value in enumerate(height):
            diff = min_value[i] - value
            if diff < 0:
                accum.append(0)
            else:
                accum.append(diff)
        #print(accum)
        return sum(accum)


sol = Solution()
#print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap(height = [5,5,1,7,1,1,5,2,7,6]))
#print(sol.trap(height = [4,2,3]))