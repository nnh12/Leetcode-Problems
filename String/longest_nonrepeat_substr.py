class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        max = 1

        for i in range(len(s)):
            count = 0

            if ( (i != len(s) -1) and s[i] != s[i+1]):
                dict = {}
                index = i
                
                while (index < len(s) and dict.get(s[index]) != 1 ):
                    dict[s[index]] = 1
                    index += 1
                    count += 1
            
            if count > max:
                max = count
    
        return max

        
