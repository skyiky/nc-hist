class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        FAIL = amount + 1
        memo = {}
        # returns the fewest number of coins needed to make up to rem target amount
        def dfs(rem: int) -> int:
            if rem == 0:
                return 0

            if rem in memo:
                return memo[rem]

            best = FAIL
            for c in coins:
                if c <= rem:
                    best = min(best, 1 + dfs(rem - c))

            memo[rem] = best
            return best

        res = dfs(amount)
        return -1 if res >= FAIL else res