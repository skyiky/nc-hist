class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # dp[i][j] = LCS length of the first i characters of text1 and first j characters of text2
        dp = [[0] * (n+1) for _ in range(m+1)]
        

        for y in range(1, m+1):
            for x in range(1, n+1):
                if text1[y-1] == text2[x-1]:
                    dp[y][x] = 1 + dp[y-1][x-1] 
                else:
                    dp[y][x] = max(dp[y-1][x], dp[y][x-1])
        
        return dp[m][n]



