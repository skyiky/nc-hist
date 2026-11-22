class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        set1 = set([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)])
        set2 = set([(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)])
        
        def bfs(visited) -> None:
            q = deque(visited)
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 
                        0 <= nc < cols and # boundary check
                        heights[nr][nc] >= heights[r][c] and # specific movement condition check
                        (nr, nc) not in visited): # visitation check
                            q.append((nr, nc))
                            visited.add((nr, nc))
        
        bfs(set1)
        bfs(set2)

        result = [[r, c] for r, c in set1 & set2]
        return result
        
        
        