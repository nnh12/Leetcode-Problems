class Solution(object):
    
    def __init__(self):
        self.list = []
        self.list_sec = []

    def generate(self, n, open, close, str):
        
        if open == n and close == n:
            self.list.append(str)
            return
        
        if open < n:
            self.generate(n, open + 1, close, str + "(")
        
        if open > close:
            self.generate(n, open, close + 1, str + ")")


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.generate(n, 0, 0, "")
        return self.list

