class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        unique = []
        repeat = []

        for i in range (len(s) - 9):
            substr = s[i:i+10]
            
            if substr not in unique:
                unique.append(substr)
            elif substr not in repeat:
                repeat.append(substr)

        return repeat
