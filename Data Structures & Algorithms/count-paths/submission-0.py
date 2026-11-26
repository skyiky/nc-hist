class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        for y in range(m):
            memo[y][0] = 1
        for x in range(n):
            memo[0][x] = 1

        for y in range(1, m):
            for x in range(1, n):
                above = memo[y-1][x]
                left = memo[y][x-1]
                memo[y][x] = above + left
        
        return memo[-1][-1]

