from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        visited = set( # unsurroundable
            [(r, 0) for r in range(rows) if board[r][0] == "O"] +
            [(0, c) for c in range(cols) if board[0][c] == "O"] +
            [(r, cols - 1) for r in range(rows) if board[r][cols - 1] == "O"] +
            [(rows - 1, c) for c in range(cols) if board[rows - 1][c] == "O"]
        )

        q = deque(visited) # BFS -> initialize queue with starting source(s)
        while q: # while unexplored "O" cells remain
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and # <<<--- CHECK IF VISITED
                    board[nr][nc] == "O"
                ):
                    visited.add((nr, nc)) # ADD TO VISIT
                    q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    board[r][c] = "X"

        return None