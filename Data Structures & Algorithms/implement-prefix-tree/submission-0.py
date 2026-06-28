class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode()
                node = node.children[char]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return True
