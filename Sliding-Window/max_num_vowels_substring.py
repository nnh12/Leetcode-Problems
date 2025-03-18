class Solution(object):

    def isVowel(self, letter):
        sett = set()
        sett = {"a", "e", "i", "o", "u"}

        if letter in sett:
            return True
        else:
            return False

    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        max_num = 0
        

        for i in range(k):
            if self.isVowel(s[i]):
                count += 1

        max_num = count
        for i in range(k, len(s)):
            
            if self.isVowel(s[i - k]):
                count -= 1
            if self.isVowel(s[i]):
                count += 1

            max_num = max(max_num, count)
        
        return max_num
            
