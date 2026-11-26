class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] = minimum coins needed to make amount a
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for rem in range(1, amount + 1):
            for c in coins:
                if c <= rem:
                    dp[rem] = min(dp[rem], 1 + dp[rem - c])
        
        if dp[amount] > amount:
            return -1
        return dp[amount]