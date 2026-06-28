class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        n = len(word)

        def dfs(i, node):
            if i == n:
                return node.endOfWord
            c = word[i]
            if c in node.children:
                return dfs(i + 1, node.children[c])
            elif c == ".":
                for child in node.children:
                    if dfs(i + 1, node.children[child]):
                        return True
                return False
            return False

        return dfs(0, node)
