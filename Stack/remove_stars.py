class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for let in s:
            if let != "*":
                stack.append(let)
            else:
                stack.pop()
        
        return ''.join(map(str, stack))
