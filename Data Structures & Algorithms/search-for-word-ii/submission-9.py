class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.word: str = None
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            curr_node = root
            for l in w:
                if l not in curr_node.children:
                    curr_node.children[l] = TrieNode()
                curr_node = curr_node.children[l]
            curr_node.word = w
        
        h, w = len(board), len(board[0])
        result = []

        def dfs(r, c, parent) -> None:
            l = board[r][c]
            if l not in parent.children:
                return

            next_parent = parent.children[l]
            
            if next_parent.word:
                result.append(next_parent.word)
                next_parent.word = None

            board[r][c] = '#'

            for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                nr, nc = dr + r, dc + c
                if (0 <= nr < h and 0 <= nc < w):
                    dfs(nr, nc, next_parent)

            board[r][c] = l


        for row in range(h):
            for col in range(w):
                dfs(row, col, root)

        return result
        