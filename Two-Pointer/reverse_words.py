class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = []
        string = ""
        low = 0
        word = 0

        for high in range(len(s)):
            if s[high] != ' ' and word == 0:
                low = high
                word = 1
            
            if s[high] == ' ' and word:
                list.append(s[low:high])
                word = 0
                
        if s[len(s) - 1] != ' ':
            list.append(s[low:len(s)])
            
        for i in range(len(list) - 1, -1, -1):
            string += list[i]
            if i != 0:
                string += " "
    
        return string
