class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        score = 0
        core = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                v = stack.pop()
                print(max(2 * v, 1), stack)
                stack[-1] += max(2 * v, 1)

        return stack.pop()
            
            
