class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        str = ""
        return_string = ""

        for let in s:
            str += let
            if let == '(':
                stack.append(let)
            else:
                stack.pop()
            
            if len(stack) == 0:
                return_string += str[1:len(str) - 1]
                str = ""

        return return_string
