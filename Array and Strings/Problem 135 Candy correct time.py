class Solution:
    def candy(self, ratings) -> int:
        '''
        There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
        '''
        n = len(ratings)
        ccandy = []
        rev_ratings = ratings[::-1]
        for i in range(n):
            ccandy.append(1)
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                ccandy[i]  = ccandy[i-1] + 1
        #ratings.reverse()
        ccandy.reverse()
        for i in range(1,n):
            if rev_ratings[i] > rev_ratings[i-1]:
                ccandy[i]  = ccandy[i-1] + 1
  
        for i in range(n-1):
            if rev_ratings[i] > rev_ratings[i+1] and ccandy[i]  <= ccandy[i+1]:
                ccandy[i]  = ccandy[i+1] + 1
        #ratings.reverse()
        ccandy.reverse()
        for i in range(n-1):
            if ratings[i] > ratings[i+1] and ccandy[i]  <= ccandy[i+1]:
                ccandy[i]  = ccandy[i+1] + 1
        return sum(ccandy)


sol = Solution()
#print(sol.candy(ratings = [1,0,2]))
#print(sol.candy(ratings = [1,2,2]))
#print(sol.candy(ratings = [1,2,87,87,87,2,1]))
#print(sol.candy(ratings = [1,3,4,5,2]))
#print(sol.candy(ratings = [1,3,2,2,1]))
#print(sol.candy(ratings = [1,6,10,8,7,3,2]))
print(sol.candy(ratings = [29,51,87,87,72,12]))