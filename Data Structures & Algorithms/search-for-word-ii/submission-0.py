class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Create Trie
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):
            char = board[r][c]
            if char not in parent.children:
                return
            
            node = parent.children[char]
            
            if node.word is not None:
                result.append(node.word)
                node.word = None # Prevent duplicate results

            board[r][c] = "#"

            for dr, dc in ((1,0), (-1,0), (0,1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and 0 <= nc < cols
                    and board[nr][nc] in node.children
                ):
                    dfs(nr, nc, node)
            
            board[r][c] = char

            if node.word is None and not node.children:
                del parent.children[char]


        for r in range(rows):
            for c in range(cols):
                if not root.children:
                    return result
                dfs(r, c, root)
        
        return result