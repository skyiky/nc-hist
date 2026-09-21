from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten_q = deque()

        h, w = len(grid), len(grid[0])

        for r in range(h):
            for c in range(w):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten_q.append((r, c))

        if fresh == 0:
            return 0
        elif not rotten_q:
            return -1
        
        time_elapsed = 0
        while rotten_q and fresh > 0:
            
            x = len(rotten_q)
            for _ in range(x):
                r, c = rotten_q.popleft()
                for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                    nr, nc = dr+r, dc+c
                    if (
                        0 <= nr < h
                        and 0 <= nc < w
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten_q.append((nr, nc))

            time_elapsed += 1

        
        return time_elapsed if fresh == 0 else -1
