class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #li = list(s.strip().split(' '))
        return len(str((list(s.strip().split(' ')))[-1]))

sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))

