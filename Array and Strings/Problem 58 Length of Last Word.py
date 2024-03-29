class Solution:
    def lengthOfLastWord(self, s) -> int:
        inp = list(s.split())
        return len(inp[-1])


sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
