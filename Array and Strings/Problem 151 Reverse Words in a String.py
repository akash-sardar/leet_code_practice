class Solution:
    def reverseWords(self, s) -> str:
        s = list(s.split())
        return " ".join(s[::-1])

sol = Solution()
print(sol.reverseWords(s="the sky is blue"))
