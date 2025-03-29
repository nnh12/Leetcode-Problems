class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        dp = [ [0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1) ]

        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1] , dp[i + 1][j ] )
        
        return dp[len(dp) - 1][len(dp[0]) - 1]
        
