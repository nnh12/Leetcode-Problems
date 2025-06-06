class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        str = ""

        for let in s:
            if let.isdigit() and stack:
                stack.pop()
            else:
                stack.append(let)
        
        for i in stack:
            str += i

        return str
