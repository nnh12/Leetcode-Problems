class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_len = float('inf')
        i = 0
        for word in strs:
            shortest_len = min(shortest_len, len(word))
            
        for i in range(shortest_len):
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    return string[0:i]

        if len(strs) == 1:
            return strs[0]
        if shortest_len == 0:
            return ""
        
        return strs[0][:i + 1]
