from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque([(amount, 0)])
        visited = { amount }

        while q:
            rem, used = q.popleft()
            for c in coins: # bfs
                nxt = rem - c
                if nxt == 0:
                    return used + 1 # nxt was the last coin we needed to get to rem == 0
                if nxt > 0 and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, used + 1))
        
        return -1

        