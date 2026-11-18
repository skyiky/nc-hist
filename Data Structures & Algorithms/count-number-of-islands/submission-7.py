from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w = len(grid[0])

        numIslands = 0
        q = deque()

        for y in range(h):
            for x in range(w):
                if grid[y][x] == "1":
                    numIslands += 1
                    grid[y][x] = "2" # mark visited

                    q.append((y, x))
                    while q:
                        y, x = q.popleft()
                        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # check neighbors
                            ny, nx = dy + y, dx + x
                            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "1": # inbounds and is an island?
                                grid[ny][nx] = "2" # mark visited
                                q.append((ny, nx))

        return numIslands
