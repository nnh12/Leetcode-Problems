class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        stack = []
        for i in range(len(word)):
            stack.append(word[i])
            if word[i] == ch:
                let = ""
                while stack:
                    let += stack.pop()
                let += word[i+1:len(word)]
                return let
        
        return word
