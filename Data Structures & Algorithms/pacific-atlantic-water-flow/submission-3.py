class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        set1 = set()
        set2 = set()
        for r in range(rows): # add left and right side tiles
            set1.add((r, 0))
            set2.add((r, cols-1))
        for c in range(cols):
            set1.add((0, c))
            set2.add((rows-1, c))
        
        def bfs(s) -> None:
            q = deque(s)
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if heights[nr][nc] >= heights[r][c]:
                            if (nr, nc) not in s:
                                q.append((nr, nc))
                                s.add((nr, nc))
        
        bfs(set1)
        bfs(set2)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in set1 and (r, c) in set2:
                    result.append([r, c])
        return result
        
        
        