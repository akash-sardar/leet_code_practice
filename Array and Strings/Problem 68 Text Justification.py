class Solution:
    def fullJustify(self, words, maxWidth):
        num_words = list(map(lambda x: len(x), words))
        rows = []
        iter = 0
        w = maxWidth
        flag = False
        while words:
            print("words", words)
            sum = 0
            row = list()
            hold = 0
            hold_index = 0

            if len(words) == 1:
                hold = len(words[0])
                hold_index = 0
                spaces_left = maxWidth - hold
                words_used = 1
                space_between_words = 0
                space_after_last_word =  spaces_left 
                row.append(words[0])
                row.append(" " * space_after_last_word)                 
            else:
                for i, word in enumerate(words):
                    if sum > w:
                        break
                    else:
                        hold = sum
                        hold_index = i-1
                        sum = sum + len(word) + 1
                spaces_left = maxWidth - hold
                words_used = hold_index + 1
                spaces_left = spaces_left + words_used 
                space_between_words = int(spaces_left / (words_used-1))
                space_after_last_word = int(spaces_left % (words_used -1 ))
                for word in range(words_used):
                    row.append(words[word])
                    if word != words_used-1:
                        row.append(" " * space_between_words)
                print("space_after_last_word", space_after_last_word)           



            rows.append(row)
            print(rows)
            #print(rows, end = "\n")
            if len(words) > 1:
                words = words[hold_index + 1:]
            else:
                words = list()
        
        result = list()
        for row in rows:
            sentence = "".join(row)
            result.append(sentence)
        return result




sol = Solution()
#print(sol.convert(s="PAYPALISHIRING", numRows = 3))
print(sol.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
