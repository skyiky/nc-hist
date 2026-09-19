class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # PREPROCESS: Build a trie so each search can follow valid prefixes
        for w in words:
            parent = root
            for l in w:
                if l not in parent.children:
                    parent.children[l] = TrieNode()
                parent = parent.children[l]
            parent.word = w
                
        h, w = len(board), len(board[0])
        result = []

        # dfs(r, c, parent) explores all valid word paths that extend parent's prefix by starting at cell (r, c), adding newly found words to result.
        # On entry:
        #   (r, c) is in bounds
        #   parent is the prefix before consuming this cell
        # During:
        #   Consume this cell if it extends the prefix
        # On return:
        #   Board is restored to entry state; found words remain in result, with their trie word markers cleared
        # Return value:
        #   None; results are collected through shared state
        def dfs(r, c, parent) -> None:
            # STATE: (r, c) is the cell to try.
            # parent represents the prefix BEFORE consuming this cell
            letter = board[r][c]

            # BASE CASE: Stop if this cell cannot extend the prefix.
            if letter not in parent.children:
                return

            # ADVANCE STATE: Consume this letter in the trie.
            curr_prefix_node = parent.children[letter]

            # RECORD SOLUTION: The current path spells a complete word.
            # Do not return: this word may be a prefix of a longer word.
            if curr_prefix_node.word is not None:
                result.append(curr_prefix_node.word)
                curr_prefix_node.word = None # # Scope: global

            # CHOOSE: Mark this cell as a used in the current path.
            board[r][c] = "#" # Scope: current path

            # EXPLORE: Try each in-bounds neighbor as the next choice.
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < h and 0 <= nc < w):
                    dfs(nr, nc, curr_prefix_node)

            # UNDO: Restore this cell for other paths
            board[r][c] = letter

        # STARTING CHOICES: A word can begin at any cell.
        # Each search starts with the empty prefix.
        for r in range(h):
            for c in range(w):
                dfs(r, c, root)
        
        return result