class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        substring = len(s)/k
        word_list = []
        num_list = []
        string = ""

        index = 0
        while index < len(s):
            word_list.append(s[index: index + k])
            index += k
        
        for word in word_list:
            score = 0
            for let in word:
                score += ord(let) - ord('a')

            num_list.append(score % 26)

        for i in num_list:
            string += (chr(i + 97))
        
        return string
