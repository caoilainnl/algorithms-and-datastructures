class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def main():
    # Create a Trie instance
    trie = Trie()

    # Test case 1: Insert words into the Trie
    print("Test Case 1: Insert Words")
    words_to_insert = ["apple", "app", "banana", "band", "bandana", "cat"]
    for word in words_to_insert:
        trie.insert(word)
        print(f"Inserted word: {word}")

    # Test case 2: Search for existing words
    print("\nTest Case 2: Search for Existing Words")
    search_words = ["apple", "app", "banana", "band", "cat"]
    for word in search_words:
        result = trie.search(word)
        print(f"Search for '{word}': {result}")
        assert result, f"'{word}' should be found in the Trie."

    # Test case 3: Search for non-existing words
    print("\nTest Case 3: Search for Non-Existing Words")
    non_existing_words = ["bat", "bandage", "can", "dog"]
    for word in non_existing_words:
        result = trie.search(word)
        print(f"Search for '{word}': {result}")
        assert not result, f"'{word}' should not be found in the Trie."

    # Test case 4: Check prefixes
    print("\nTest Case 4: Check Prefixes")
    prefixes = ["app", "ban", "band", "c", "bat"]
    expected_results = [True, True, True, True, False]
    for prefix, expected in zip(prefixes, expected_results):
        result = trie.starts_with(prefix)
        print(f"Starts with '{prefix}': {result}")
        assert result == expected, f"Prefix '{prefix}' result mismatch. Expected {expected}."

    print("\nAll test cases passed!")

if __name__ == "__main__":
    main()
