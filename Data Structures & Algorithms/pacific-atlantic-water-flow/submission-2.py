from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h, w = len(heights), len(heights[0])
        
        def bfs(starts):
            visited = set(starts)
            q = deque(visited)

            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < h and 
                        0 <= nc < w and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited

        pacific = bfs([(0, c) for c in range(w)] + [(r, 0) for r in range(h)])
        atlantic = bfs([(h - 1, c) for c in range(w)] + [(r, w - 1) for r in range(h)])

        return [[r, c] for r, c in pacific & atlantic]
