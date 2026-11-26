class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for y in range(1, m):
            for x in range(1, n):
                above = dp[y-1][x]
                left = dp[y][x-1]
                dp[y][x] = above + left
        
        return dp[-1][-1]

