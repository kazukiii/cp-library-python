class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.count = 0  # Number of words passing through this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # Increment count each time we pass through a node
        node.is_end_of_word = True

    def search(self, word):
        node = self._search_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix):
        return self._search_node(prefix) is not None

    def count_words_equal_to(self, word):
        node = self._search_node(word)
        return node.count if node and node.is_end_of_word else 0

    def count_words_starting_with(self, prefix):
        node = self._search_node(prefix)
        return node.count if node else 0

    def _search_node(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def erase(self, word):
        self._erase(self.root, word, 0)

    def _erase(self, node, word, index):
        if index == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
                node.count -= 1
            return node.count == 0
        char = word[index]
        if char in node.children and self._erase(node.children[char], word, index + 1):
            node.children.pop(char)
            return not node.children and not node.is_end_of_word
        node.count -= 1
        return node.count == 0


if __name__ == "__main__":
    # Usage
    trie = Trie()
    trie.insert("hello")
    trie.insert("hell")
    trie.insert("helium")

    print(trie.search("hello"))  # True
    print(trie.count_words_equal_to("hello"))  # 1
    print(trie.count_words_starting_with("hel"))  # 3
    print(trie.starts_with("he"))  # True
