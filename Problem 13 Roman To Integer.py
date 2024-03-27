class Solution:
    def romanToInt(self, s) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        s = list(s)
        n = len(s)
        accum = list()
        for i, value in enumerate(s):
            accum.append(roman[value])
            if value in ["V", "X"]:
                if s[i-1] == 'I' and i > 0:
                    accum[i-1] = 0
                    accum[i] = accum[i] - 1
            if value in ["L", "C"]:
                if s[i-1] == 'X' and i > 0:
                    accum[i-1] = 0
                    accum[i] = accum[i] - 10                    
            if value in ["D", "M"]:
                if s[i-1] == 'C' and i > 0:
                    accum[i-1] = 0
                    accum[i] = accum[i] - 100
        return sum(accum)
        






sol = Solution()
#print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.romanToInt(s = "MCMXCIV"))
#print(sol.trap(height = [4,2,3]))