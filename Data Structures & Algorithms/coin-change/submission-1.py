class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        impossible = amount + 1
        memo = {}
        # returns the fewest number of coins needed to make up to rem target amount
        def dfs(rem: int) -> int:
            if rem == 0:
                return 0

            if rem in memo:
                return memo[rem]

            used = impossible
            for coin in coins:
                if coin <= rem:
                    used = min(used, 1 + dfs(rem - coin))

            memo[rem] = used
            return used

        ans = dfs(amount)
        return -1 if ans >= impossible else ans