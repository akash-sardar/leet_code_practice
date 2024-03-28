class Solution:
    def longestCommonPrefix(self, strs) -> str:
        lengths = list(map(lambda x: len(x),strs))
        min_val = min(lengths)
        index = lengths.index(min_val)
        hold = strs[index]
        while hold:
            #print(hold)
            flag = False
            for word in strs:
                if word.startswith(hold):
                    flag = True
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                return hold
            hold = list(hold)
            hold.pop()
            hold = "".join(hold)
        return ""





# MMMDCCXCIV
sol = Solution()
print(sol.longestCommonPrefix(strs = ["flower","flow"]))
