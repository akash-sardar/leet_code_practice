class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        s = list(s[:])
        row = list()
        start = 0
        end = numRows
        iter = 0
        while s:
            if iter == 0 or iter % 2 == 0:
                    row.append(s[start:end])
                    s = s[end:]
                    iter = iter + 1
                
            else:
                    #row.append(" ")
                    tokens = s[start:end-2][::-1]
                    tokens.insert(0, "<PAD>")
                    tokens.append("<PAD>")
                    row.append(tokens)
                    #row.append(" ")
                    s = s[end-2:]
                    iter = iter + 1

        for idx in range(len(row)):
            if len(row[idx]) != numRows:
                n = len(row[idx])
                diff = numRows-n
                for i in range(diff):
                    row[idx].append("<PAD>")


        #print(row)
        zipped_rows = list(zip(*row))
        #print(zipped_rows)
        result = ""
        for i in zipped_rows:
            for j in i:
                if j != "<PAD>":
                    result = result + j
        return result



sol = Solution()
#print(sol.convert(s="PAYPALISHIRING", numRows = 3))
print(sol.convert(s="ABCDE", numRows = 4))
