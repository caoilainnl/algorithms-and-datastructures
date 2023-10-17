class KMPAlgorithm:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lps = self.compute_lps(pattern)

    def compute_lps(self, pattern):
        """
        Computes the Longest Prefix Suffix (LPS) array.
        LPS[i] stores the length of the longest prefix of the pattern that is also a suffix for pattern[0..i].
        """
        lps = [0] * len(pattern)
        length = 0  # Length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def search(self, text):
        """
        Finds all occurrences of the pattern in the text using the KMP algorithm.
        Returns a list of starting indices of matches.
        """
        result = []
        m, n = len(self.pattern), len(text)
        i, j = 0, 0  # i for text, j for pattern

        while i < n:
            if self.pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                result.append(i - j)  # Match found
                j = self.lps[j - 1]
            elif i < n and self.pattern[j] != text[i]:
                if j != 0:
                    j = self.lps[j - 1]
                else:
                    i += 1

        return result


# Testing the implementation
def main():
    print("Running exhaustive tests for KMP Algorithm...")

    # Test Case 1: Basic string matching
    print("\nTest Case 1: Basic string matching")
    text = "ababcabcabababd"
    pattern = "ababd"
    kmp = KMPAlgorithm(pattern)
    print(f"Matches for '{pattern}' in '{text}' (Expected [10]): {kmp.search(text)}")

    # Test Case 2: Multiple occurrences
    print("\nTest Case 2: Multiple occurrences")
    text = "aaabaaabaaa"
    pattern = "aaab"
    kmp = KMPAlgorithm(pattern)
    print(f"Matches for '{pattern}' in '{text}' (Expected [0, 4]): {kmp.search(text)}")

    # Test Case 3: No matches
    print("\nTest Case 3: No matches")
    text = "abcdefgh"
    pattern = "ijk"
    kmp = KMPAlgorithm(pattern)
    print(f"Matches for '{pattern}' in '{text}' (Expected []): {kmp.search(text)}")

    # Test Case 4: Pattern larger than text
    print("\nTest Case 4: Pattern larger than text")
    text = "short"
    pattern = "toolongpattern"
    kmp = KMPAlgorithm(pattern)
    print(f"Matches for '{pattern}' in '{text}' (Expected []): {kmp.search(text)}")

    # Test Case 5: Pattern matches entire text
    print("\nTest Case 5: Pattern matches entire text")
    text = "perfectmatch"
    pattern = "perfectmatch"
    kmp = KMPAlgorithm(pattern)
    print(f"Matches for '{pattern}' in '{text}' (Expected [0]): {kmp.search(text)}")

    # Test Case 6: Pattern appears at the end of text
    print("\nTest Case 6: Pattern appears at the end of text")
    text = "thisisaverylongtextendingwithpattern"
    pattern = "pattern"
    kmp = KMPAlgorithm(pattern)
    print(f"Matches for '{pattern}' in '{text}' (Expected [27]): {kmp.search(text)}")

    # Test Case 7: Pattern with overlapping occurrences
    print("\nTest Case 7: Pattern with overlapping occurrences")
    text = "aaaaa"
    pattern = "aaa"
    kmp = KMPAlgorithm(pattern)
    print(f"Matches for '{pattern}' in '{text}' (Expected [0, 1, 2]): {kmp.search(text)}")

    # Test Case 8: Empty text or pattern
    print("\nTest Case 8: Empty text or pattern")
    text = ""
    pattern = "abc"
    kmp = KMPAlgorithm(pattern)
    print(f"Matches for '{pattern}' in empty text (Expected []): {kmp.search(text)}")
    text = "some text"
    pattern = ""
    kmp = KMPAlgorithm(pattern)
    print(f"Matches for empty pattern in '{text}' (Expected []): {kmp.search(text)}")


if __name__ == "__main__":
    main()
