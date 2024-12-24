# Input: s = "()[]{}"
# Output: true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_char = ['(',  '{', '[']
        close_char = [')',  '}', ']']

        for letter in s:
            if letter in close_char and not stack:
                return False
            if letter in open_char:
                stack.append(letter)
            elif letter == '}':
                top = stack.pop()
                if top != '{':
                    return False
            elif letter == ']':
                top = stack.pop()
                if top != '[':
                    return False
            elif letter == ')':
                top = stack.pop()
                if top != '(':
                    return False
        
        if stack:
            return False
        else:
            return True
                   



