class Solution:
    def uniquePaths_TD_Prefix(self, m: int, n: int) -> int:
        memo = {}
        def dfs(y, x) -> int:
            if y < 0 or x < 0:
                return 0
            if y == 0 and x == 0:
                return 1
            if (y, x) in memo:
                return memo[(y, x)]
            
            memo[((y, x))] = dfs(y-1, x) + dfs(y, x-1)
            return memo[(y, x)]
        return dfs(m-1, n-1)

    def uniquePaths_TD_Suffix(self, m: int, n: int) -> int:
        memo = {}
        def dfs(y, x) -> int:
            if y >= m or x >= n:
                return 0
            if y == m-1 and x == n-1:
                return 1
            if (y, x) in memo:
                return memo[(y, x)]
            
            memo[((y, x))] = dfs(y+1, x) + dfs(y, x+1)
            return memo[(y, x)]
        return dfs(0, 0)
    
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePaths_TD_Suffix(m, n)


















    def uniquePathsBottomUp(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1] # above + left
        
        return dp[-1][-1]
