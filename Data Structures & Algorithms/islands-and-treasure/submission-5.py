from collections import deque

# Multi-source BFS
#   Put all starting points in one queue with distance 0
#   Expand outward in layers
#   On first reaching a cell, record its distance and enqueue it, never visit it again
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        h, w = len(grid), len(grid[0])
        LAND = 2147483647
        CHEST = 0
        q = deque()

        for r in range(h):
            for c in range(w):
                if grid[r][c] == CHEST:
                    q.append((r ,c))
          
        while q:
            row, col = q.popleft()
         
            for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < h and 
                    0 <= nc < w and
                    grid[nr][nc] == LAND
                ):
                    grid[nr][nc] = grid[row][col] + 1 #  The grid stores the answer and the search state.
                    q.append((nr, nc))
            
       