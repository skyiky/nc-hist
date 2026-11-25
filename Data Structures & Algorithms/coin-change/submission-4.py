from collections import deque

class Solution:
    # Because every coin adds weight 1, Coin Change is an unweighted shortest-path problem from amount to 0. BFS has the same worst-case complexity, but exits early when the answer is small (e.g., coins = [1, 5000], amount = 10000 finishes in 2 levels instead of computing all 10,000 states).
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        q = deque([(amount, 0)]) # (remaining_amount, coins_used)
        visited = { amount } # the first time BFS reaches any amount nxt, it did so with the minimum possible coins, so we never need to revisit nxt
        
        while q:
            rem, used = q.popleft()

            for c in coins:
                nxt = rem - c
                if nxt == 0:
                    return used + 1
                if nxt > 0 and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, used + 1))
        
        return -1




    def coinChangeDFS(self, coins: List[int], amount: int) -> int:
        IMPOSSIBLE = amount + 1
        memo = {}
        # returns the fewest number of coins needed to make up to rem target amount
        def dfs(rem: int) -> int:
            if rem == 0:
                return 0

            if rem in memo:
                return memo[rem]

            best = IMPOSSIBLE
            for c in coins:
                if c <= rem:
                    best = min(best, 1 + dfs(rem - c))

            memo[rem] = best
            return best

        res = dfs(amount)
        return -1 if res >= IMPOSSIBLE else res