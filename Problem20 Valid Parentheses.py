'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''


class Solution:
    def isValid(self, s: str) -> bool:
        brace_dict = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        for brace in s:
            if brace not in brace_dict:
                stack.append(brace)
            else:
                if stack:
                    last_element = stack.pop()
                    if brace_dict.get(brace) != last_element:
                        return False
                else:
                    return False

        if stack:
            return False
        else:
            return True


sol = Solution()
print(sol.isValid('([)]'))
# (([]){})
# ([)]
