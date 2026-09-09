class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        visited = set()
        
        # backtrack(row, col, i) checks whether this cell can match word[i], then whether a neighboring path can finish the word.
        def backtrack(row, col, i) -> bool:
            if (not (0 <= row < len(board) and 0 <= col < len(board[0]))
                or (row, col) in visited
                or board[row][col] != word[i]):
                return False

            if i == len(word) - 1:
                return True
            visited.add((row, col))
            result = (
                backtrack(row-1, col, i+1)
                or backtrack(row+1, col, i+1)
                or backtrack(row, col-1, i+1)
                or backtrack(row, col+1, i+1)
            )
            visited.remove((row, col))
            return result


        for row in range(h):
            for col in range(w):
                if backtrack(row, col, 0):
                    return True

        return False
