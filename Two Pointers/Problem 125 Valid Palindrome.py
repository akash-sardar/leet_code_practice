import re

class Solution:
    def isPalindrome(self, s) -> bool:
        s = re.findall("[a-zA-Z0-9]",s)
        s = "".join(s)
        s = s.lower()
        return s == s[::-1]


sol = Solution()
#print(sol.convert(s="PAYPALISHIRING", numRows = 3))
print(sol.isPalindrome(s = "A man, a plan, a canal: Panama"))
