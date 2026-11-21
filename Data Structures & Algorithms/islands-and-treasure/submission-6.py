from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        LAND = 2147483647
        CHEST = 0
        WATER = -1

        q = deque()
        num_land = 0
        # find all treasure first
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == CHEST:
                    q.append((r, c))
                elif grid[r][c] == LAND:
                    num_land += 1

        # edge case where no land
        if num_land == 0:
            return None
        
        distance = 1
        while q: 
            i = len(q)
            for _ in range(i): # for each starting treasure position
                r, c = q.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc # neighbor position
                    if 0 <= nr < rows and 0 <= nc < cols: # boundary check
                        if grid[nr][nc] == LAND: # if neighbor is land
                            grid[nr][nc] = distance # update tile value to distance
                            q.append((nr, nc)) # only continue traverse from land tiles
            distance += 1 # increment distance before starting next turn

        return None
    