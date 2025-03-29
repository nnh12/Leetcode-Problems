class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s) + 1):
            for word in wordDict:
                start = i - len(word) + 1
                if start >= 0 and dp[start] and s[start : start + len(word) ] == word:
                    dp[i + 1] = True
                    break
        
        return dp[len(s)]
