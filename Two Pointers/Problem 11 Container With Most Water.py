class Solution:
    def threeSum(self, nums):
        bucket= sorted(nums)
        a_hold = None
        results = []
        for i, a in enumerate(bucket):
            if a_hold != a:
                a_hold = a
                inner_bucket = bucket[i:]
                l = 0
                r = -1
                while len(inner_bucket)> 1 :
                    if a + inner_bucket[l] + inner_bucket[r] == 0:
                        results.append([a, inner_bucket[l], inner_bucket[r]])
                        inner_bucket = inner_bucket[1:-1]
                    elif a + inner_bucket[l] + inner_bucket[r] > 0:
                        inner_bucket = inner_bucket[:-1]
                    else:
                        inner_bucket = inner_bucket[1:]
        results = set(*results)
        return results