class Solution:
    def intToRoman(self, num: int) -> str:
        arabic = [1000, 500, 100, 50, 10, 5, 1]
        roman = ["M", "D", "C", "L", "X", "V", "I"]
        s = num
        factors = list()
        while s:
            if s >= 1000:
                factor =  int(s/1000)
                s = int(s % 1000)
                factors.append(factor * "M")
                continue

            if s >= 900:
                factors.append("CM")
                s = int(s % 900)
                continue

            if s >=500:
                factor = int(s/500)
                s = int(s % 500)
                factors.append("D" * factor)
                continue

            if s >=400:
                factors.append("CD")
                factor = int(s/400)
                s = int(s%400)
                continue

            if s >=100:
                factor = int(s/100)
                s = int(s % 100)
                factors.append("C" * factor)
                continue

            if s >=90:
                factor = int(s/90)
                s = int(s % 90)
                factors.append("XC")
                continue    

            if s >=50:
                factor = int(s/50)
                s = int(s % 50)
                factors.append("L" * factor)
                continue  

            if s >=40:
                factor = int(s/40)
                s = int(s % 40)
                factors.append("XL")
                continue 

            if s >=10:
                factor = int(s/10)
                s = int(s % 10)
                factors.append("X" * factor)
                continue 

            if s >=9:
                factor = int(s/9)
                s = int(s % 9)
                factors.append("IX")
                continue

            if s >=5:
                factor = int(s/5)
                s = int(s % 5)
                factors.append("V" * factor)
                continue

            if s >=4:
                factor = int(s/4)
                s = int(s % 4)
                factors.append("IV")
                continue   

            if s < 4 and s > 0:
                factor = int(s/5)
                s = int(s % 5)
                factors.append("I" * s)
                s = None
                continue

            if s == 0:
                s = None
                break
        return ''.join(factors)



# MMMDCCXCIV
sol = Solution()
#print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.intToRoman(num = 3794))
#print(sol.trap(height = [4,2,3]))