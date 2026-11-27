# Both approaches have the exact same dependencies (a bigger problem depends on smaller subproblems). The only difference is which end you start from.
# 
# Top-down mental model = SEPARATE the two directions:
# - Going DOWN (parameters): You pass down constraints ("where am I now?" = i, "what limits my future choices?" = j).
# - Coming UP (return values): Base cases return 0, each "pick" branch "adds" on the way back up, and each node returns the max of its children.
# 	- Answers resolve coming UP
# 
# 
# Top-down starts at the big problem, asks for smaller subproblems that are not solved yet, and resolves answers coming back up from the base cases.
# Bottom-up starts at the base cases and loops in an order where every smaller subproblem you look up is already solved in the table.
# 
# Top-down = Big problem  ──(calls)──▶  ...  ──(calls)──▶  Base case
#            Big problem  ◀─(returns)─  ...  ◀─(returns)─  Base case
#                                                          
# Bottom-Up = Base case  ──▶  Small  ──▶  Medium  ──▶  Big problem
# Bottom-up starts at the base cases and loops in an order where every smaller subproblem you look up is already solved in the table.
#                                                    	
# - Top-Down → Prefix (when working backward from a target) or Suffix (when simulating decisions forward)
# - Bottom-Up → Prefix (clean forward loops)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePaths_TD_Prefix(m, n)

    def uniquePaths_TD_Prefix(self, m: int, n: int) -> int:
        memo = {}
        def dfs(y, x) -> int:
            if y < 0 or x < 0:
                return 0
            if y == 0 and x == 0:
                return 1
            if (y, x) in memo:
                return memo[(y, x)]
            
            memo[(y, x)] = dfs(y-1, x) + dfs(y, x-1)
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
            
            memo[(y, x)] = dfs(y+1, x) + dfs(y, x+1)
            return memo[(y, x)]
        return dfs(0, 0)

    def uniquePaths_BU_Prefix(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[m-1][n-1]

    def uniquePaths_BU_Suffix(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for y in reversed(range(m-1)):
            for x in reversed(range(n-1)):
                dp[y][x] = dp[y + 1][x] + dp[y][x + 1]
        return dp[0][0]
        