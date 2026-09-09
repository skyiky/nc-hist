class Solution:
    # DFS describes the exploration order; backtracking describes how you manage candidate choices. Backtracking is commonly implemented using DFS.
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        visited = set()
        
        if len(word) > h * w:
            return False

        # dfs(row, col, i) checks whether this cell can match word[i], then whether a neighboring path can finish the word.
        def dfs(row, col, i) -> bool:
            if (not (0 <= row < len(board) and 0 <= col < len(board[0]))
                or (row, col) in visited
                or board[row][col] != word[i]):
                return False

            if i == len(word) - 1:
                return True
            
            visited.add((row, col))
            # original = board[row][col]
            # board[row][col] = "#" <-- Alternative to using visited set

            result = (
                dfs(row-1, col, i+1)
                or dfs(row+1, col, i+1)
                or dfs(row, col-1, i+1)
                or dfs(row, col+1, i+1)
            )
            visited.remove((row, col))
            # board[row][col] = original <-- Alternative to using visited set
            return result


        for row in range(h):
            for col in range(w):
                if dfs(row, col, 0):
                    return True

        return False
