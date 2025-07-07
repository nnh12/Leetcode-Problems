class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        cache = {}
        cache['2'] = "abc"
        cache['3'] = "def"
        cache['4'] = "ghi"
        cache['5'] = "jkl"
        cache['6'] = "mno"
        cache['7'] = "pqrs"
        cache['8'] = "tuv"
        cache['9'] = "wxyz"
        res = []

        def helper(index, str):
            if len(str) == len(digits):
                res.append(str)
                return
            
            for c in cache[digits[index]]:
                helper(index + 1, str + c)
            
        helper(0, "")
        if len(digits) == 0:
            return []
        return res
