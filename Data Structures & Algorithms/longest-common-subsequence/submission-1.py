class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        def BU(m, n) -> int:
            # dp[i][j] = LCS length of the first i characters of text1 and first j characters of text2
            dp = [[0] * (n+1) for _ in range(m+1)]

            for y in range(1, m+1):
                for x in range(1, n+1):
                    if text1[y-1] == text2[x-1]:
                        dp[y][x] = 1 + dp[y-1][x-1] 
                    else:
                        dp[y][x] = max(dp[y-1][x], dp[y][x-1])

            return dp[m][n]
        
        memo = {}
        # dfs(i, j) = LCA of text1[:i) and text2[:j)
        def dfs(i: int, j: int) -> int:
            if i == -1 or j == -1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i-1, j-1)    
            else:
                memo[(i, j)] = max(dfs(i-1, j), dfs(i, j-1))
            return memo[(i, j)]

        return dfs(m-1, n-1)



