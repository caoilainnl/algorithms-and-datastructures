class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def main():
    # Create a UnionFind instance
    n = 10  # Number of elements (0 to 9)
    uf = UnionFind(n)

    # Test case 1: Union operations and connectivity checks
    print("Test Case 1: Union and Connectivity")
    connections = [(1, 2), (2, 3), (4, 5), (6, 7)]
    for x, y in connections:
        uf.union(x, y)
        print(f"Union({x}, {y})")

    connectivity_checks = [(1, 3), (4, 5), (6, 7), (1, 5), (3, 6)]
    expected_results = [True, True, True, False, False]
    for (x, y), expected in zip(connectivity_checks, expected_results):
        result = uf.connected(x, y)
        print(f"Connected({x}, {y}): {result}")
        assert result == expected, f"Connectivity check for ({x}, {y}) failed. Expected {expected}."

    # Test case 2: Path compression
    print("\nTest Case 2: Path Compression")
    uf.union(5, 6)  # Connect two existing groups
    print(f"Union(5, 6)")
    assert uf.connected(4, 7), "4 and 7 should now be connected after Union(5, 6)."
    print("Connected(4, 7):", uf.connected(4, 7))

    # Test case 3: Self-connectivity
    print("\nTest Case 3: Self-Connectivity")
    for i in range(n):
        assert uf.connected(i, i), f"Element {i} should always be connected to itself."
        print(f"Connected({i}, {i}): True")

    # Test case 4: Isolated elements
    print("\nTest Case 4: Isolated Elements")
    isolated_checks = [(0, 1), (8, 9)]
    for x, y in isolated_checks:
        result = uf.connected(x, y)
        print(f"Connected({x}, {y}): {result}")
        assert not result, f"Connectivity check for ({x}, {y}) failed. Expected False."

    print("\nAll test cases passed!")

if __name__ == "__main__":
    main()
