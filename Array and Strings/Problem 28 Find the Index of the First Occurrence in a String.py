class Solution:
    def strStr(self, haystack, needle) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1



sol = Solution()
#print(sol.convert(s="PAYPALISHIRING", numRows = 3))
print(sol.strStr(haystack = "sadbutsad", needle = "sad"))
