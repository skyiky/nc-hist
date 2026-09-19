class TrieNode():
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, start):
            for i in range(start, len(word)):
                c = word[i]
                if c == '.':
                    for n in node.children.values():
                        if dfs(n, i+1):
                            return True
                    return False
                elif c not in node.children:
                    return False
                else:
                    node = node.children[c]
            return node.is_word

        return dfs(self.root, 0)

        
