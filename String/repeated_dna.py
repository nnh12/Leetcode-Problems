class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        unique = {}
        repeat = []

        for i in range (len(s) - 9):
            substr = s[i:i+10]
            
            if substr not in unique:
                unique[substr] = 1
            elif substr not in repeat:
                repeat.append(substr)

        return repeat
