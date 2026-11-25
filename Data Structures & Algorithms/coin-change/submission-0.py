class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        # returns the fewest number of coins needed to make up to rem target amount
        def dfs(rem: int) -> int:
            if rem == 0:
                return 0
            
            if rem in memo:
                return memo[rem]

            used = float('inf')
            
            for coin in coins:
                if coin <= rem:
                    result = dfs(rem - coin)
                    if result != -1:
                        used = min(used, 1 + result)

            if used == float('inf'):
                used = -1

            memo[rem] = used
            return memo[rem]

        return dfs(amount)