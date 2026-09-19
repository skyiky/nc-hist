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