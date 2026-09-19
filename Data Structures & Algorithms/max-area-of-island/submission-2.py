class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                curr_size = 1
                grid[r][c] = 0
                stack = [(r, c)]

                while stack:
                    row, col = stack.pop()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = row + dr, col + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                        ):
                            curr_size += 1
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
                result = max(result, curr_size)

        return result