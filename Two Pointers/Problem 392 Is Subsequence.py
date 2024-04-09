import re

class Solution:
    def isSubsequence(self, s, t) -> bool:
        s = list(s[:])
        t = list(t[:])
        for i in s:
            if i in t:
                idx = t.index(i)
                t = t[idx+1:]
                continue
            else:
                return False
        return True


sol = Solution()
#print(sol.convert(s="PAYPALISHIRING", numRows = 3))
print(sol.isSubsequence(s = "aaaaaa", t = "bbaaaa"))
