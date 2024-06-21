class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # edge cases
        if len(s) == 0 or s is None or words is None:
            return []
        
        # intialize variables
        count = {} # dicitonary that keeps (word, count)
        wordLength = len(words[0])  # all words are of same length
        res = []  # result list
        wordsLength = len(words) * wordLength # length of the list times length of the word

        # fill out our count dictionary
        for word in words:
            count[word] = count.get(word, 0) + 1
        
        # go find substrings that answer the question
        for left in range(len(s) - wordsLength + 1):
            # dicitonary that keeps track of the words we find in our sliding window
            wordsSeen = {}
            # make a right bound - iterate through it to find words
            for right in range(len(words)):
                # tis tells us where our word will start
                wordIndex = left + right * wordLength
                tempWord = s[wordIndex : wordIndex + wordLength]
                if tempWord not in count:
                    break
                wordsSeen[tempWord] = wordsSeen.get(tempWord, 0) + 1
                if wordsSeen[tempWord] > count[tempWord]:
                    break
            if wordsSeen == count:
                res.append(left)
        return res








sol = Solution()
print(sol.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
