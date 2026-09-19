class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)] 
        result = []

        def diagonal(row, col) -> list:
            diag = []
            # left and up
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                diag.append(board[r][c])
                r -= 1
                c -= 1
            # left and down
            r, c = row + 1, col - 1
            while r < n and c >= 0:
                diag.append(board[r][c])
                r += 1
                c -= 1
            return diag

        # dfs(col): 
        # 1. Assumes columns [0, col) each have one queen, with no conflicts
        # 2. Tries every valid placement in column col, then calls dfs(col + 1)
        # 3. Appends a snapshot of each complete valid board to result
        # 4. Restores board to exactly how it was when this call started
        def dfs(col: int) -> None:
            if col == n:
                result.append(["".join(row) for row in board[:]])
                return
            
            for row in range(n):
                if ("Q" not in board[row]
                    and "Q" not in diagonal(row, col)):
                    board[row][col] = "Q"
                    dfs(col + 1)
                    board[row][col] = "."

        dfs(0)
        return result