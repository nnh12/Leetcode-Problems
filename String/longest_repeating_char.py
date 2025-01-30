class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        max  = 0 

        for i in range(len(s)):
            start = s[i]
            iterate = i
            cur_count = 0
            replac_count = k

            while (iterate < len(s) and (start == s[iterate] or replac_count > 0) ):
                if (start != s[iterate]):
                    replac_count -= 1
                
                iterate += 1
                cur_count += 1
            
            if cur_count > max:
                max = cur_count
        
        return max

