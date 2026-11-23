from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        rows = len(grid)
        cols = len(grid[0])

        pacific = set([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)])
        atlantic = set([(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)])

        def bfs(visited) -> None:
            q = deque(visited)
            while q:
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and 
                        0 <= nc < cols and
                        grid[nr][nc] >= grid[r][c] and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        bfs(pacific)
        bfs(atlantic)

        return [[r, c] for (r, c) in pacific & atlantic]

        
