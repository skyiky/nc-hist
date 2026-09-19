class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Create Trie
        for word in words:
            x = root
            for letter in word:
                if letter not in x.children:
                    x.children[letter] = TrieNode()
                x = x.children[letter]
            x.word = word
                
        h, w = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):
            letter = board[r][c]
            if letter not in parent.children:
                return

            node = parent.children[letter]

            if node.word is not None:
                result.append(node.word)
                node.word = None

            board[r][c] = "#" # prevent cyclical traversal for current word

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < h and 0 <= nc < w):
                    next_candidate_letter = board[nr][nc] 
                    if next_candidate_letter in node.children:
                        dfs(nr, nc, node)

            board[r][c] = letter

        for r in range(h):
            for c in range(w):
                dfs(r, c, root)
        
        return result