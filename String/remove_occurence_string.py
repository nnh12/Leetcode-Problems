class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while part in s:
            index = s.find(part)
            s = s[:index] + s[index + len(part) ::]
        
        return s

        
