# Apply this to: Count connected regions in a grid or graph, 
#   where each region contains items reachable from one another through allowed moves.
# count = 0
# visited = set()
#
# for each cell:
#    if cell is invalid or already visited:
#        continue
#
#    count += 1
#    mark cell visited
#    stack = [cell]
#
#    while stack is not empty:
#        current = stack.pop()
#
#        for each neighbor of current:
#            if neighbor is valid and not visited:
#                mark neighbor visited
#                stack.push(neighbor)
#
# return count
# Key rule: Mark a cell visited when pushing it, not when popping it.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue

                islands += 1
                grid[r][c] = "0"
                stack = [(r, c)]

                while stack:
                    row, col = stack.pop()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = row + dr, col + dc

                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == "1"
                        ):
                            grid[nr][nc] = "0"
                            stack.append((nr, nc))

        return islands
