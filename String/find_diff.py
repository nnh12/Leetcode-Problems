class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        first = {}

        for i in s:
            if i not in first:
                first[i] = 1
            else:
                first[i] += 1

        for i in t:
            if i not in first or first[i] == 0:
                print(first)
                return i
            else:
                first[i] -= 1
        
        return ""
