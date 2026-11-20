from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        num_fresh = 0
        list_rotten = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    list_rotten.append((r, c))
        
        if len(list_rotten) == 0 and num_fresh > 0:
            return -1

        print(num_fresh, len(list_rotten))

        minutes = 0
        while num_fresh > 0 and list_rotten: # only continue if there are still fresh fruit + making progress
            num_rots_this_turn = len(list_rotten)
            for _ in range(num_rots_this_turn):
                r, c = list_rotten.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        print(f"ROTTING y:{nr}, x:{nc}, TURN: {minutes}")
                        list_rotten.append((nr, nc))
                        grid[nr][nc] = 2
                        num_fresh -= 1
            minutes += 1            

        print(num_fresh, len(list_rotten))

        if num_fresh == 0:
            return minutes
        else:
            return -1



            


        
        