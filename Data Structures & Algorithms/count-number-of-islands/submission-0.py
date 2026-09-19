class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visited = set()

        def dfs(row, col) -> bool:
            if (
                not(0 <= row < len(grid)) or
                not(0 <= col < len(grid[0])) or
                (row, col) in visited):
                return False
            p = grid[row][col]
            if p == "0":
                return False
            if p == "1":
                visited.add((row, col))
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    dfs(row + dr, col + dc)
                return True


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if dfs(row, col):
                    result += 1
        
        return result
