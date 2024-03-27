class Solution:
    def candy(self, ratings) -> int:
        n = len(ratings)
        ccandy = []
        for i in range(n):
            if i == 0:
                ccandy.append(1)
                print(ratings[:i+1], ':', ccandy)
            else:
                if ratings[i] > ratings[i-1]:
                    ccandy.append(ccandy[i-1]+1)
                elif ratings[i] < ratings[i-1]:
                    if (ccandy[i-1]) == 1:
                        ccandy[i-1] += 1
                        ccandy.append(1)
                        for j in reversed(range(i)):
                            if ccandy[j] == ccandy[j-1] and ratings[j] != ratings[j-1]:
                                ccandy[j-1] += 1
                                print('reset',ratings[:i+1], ':', ccandy)
                            else:
                                break
                    else:
                        ccandy.append(1)
                else:
                    ccandy.append(1)

                print(ratings[:i+1], ':', ccandy)
        return sum(ccandy)


sol = Solution()
#print(sol.candy(ratings = [1,0,2]))
#print(sol.candy(ratings = [1,2,2]))
#print(sol.candy(ratings = [1,2,87,87,87,2,1]))
#print(sol.candy(ratings = [1,3,4,5,2]))
#print(sol.candy(ratings = [1,3,2,2,1]))
#print(sol.candy(ratings = [1,6,10,8,7,3,2]))
#print(sol.candy(ratings = [29,51,87,87,72,12]))