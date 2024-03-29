class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

sol = Solution()
print(sol.strStr("sadbutsad", "sad")

