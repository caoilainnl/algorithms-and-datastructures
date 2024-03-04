import math

class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        self.log = [0] * (self.n + 1)
        self.build_log()
        self.st = [[0] * (self.log[self.n] + 1) for _ in range(self.n)]
        self.build_sparse_table(arr)

    def build_log(self):
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

    def build_sparse_table(self, arr):
        for i in range(self.n):
            self.st[i][0] = arr[i]
        
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.st[i][j] = min(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def range_min_query(self, l, r):
        j = self.log[r - l + 1]
        return min(self.st[l][j], self.st[r - (1 << j) + 1][j])


# Testing the implementation
def main():
    print("Running exhaustive tests for Sparse Table...")

    # Test Case 1: Basic range queries
    print("\nTest Case 1: Basic range queries")
    arr = [1, 3, 2, 7, 9, 11, 3, 5]
    sparse_table = SparseTable(arr)
    print(f"RMQ(0, 3) (Expected 1): {sparse_table.range_min_query(0, 3)}")
    print(f"RMQ(2, 5) (Expected 2): {sparse_table.range_min_query(2, 5)}")
    print(f"RMQ(4, 7) (Expected 3): {sparse_table.range_min_query(4, 7)}")

    # Test Case 2: Full range query
    print("\nTest Case 2: Full range query")
    print(f"RMQ(0, 7) (Expected 1): {sparse_table.range_min_query(0, 7)}")

    # Test Case 3: Single element range
    print("\nTest Case 3: Single element range")
    print(f"RMQ(3, 3) (Expected 7): {sparse_table.range_min_query(3, 3)}")
    print(f"RMQ(6, 6) (Expected 3): {sparse_table.range_min_query(6, 6)}")

    # Test Case 4: Edge cases with smallest and largest indices
    print("\nTest Case 4: Edge cases")
    print(f"RMQ(0, 0) (Expected 1): {sparse_table.range_min_query(0, 0)}")
    print(f"RMQ(7, 7) (Expected 5): {sparse_table.range_min_query(7, 7)}")

    # Test Case 5: Larger array
    print("\nTest Case 5: Larger array")
    large_arr = [i for i in range(100, 0, -1)]  # Descending array
    large_sparse_table = SparseTable(large_arr)
    print(f"RMQ(0, 99) (Expected 1): {large_sparse_table.range_min_query(0, 99)}")
    print(f"RMQ(50, 99) (Expected 1): {large_sparse_table.range_min_query(50, 99)}")
    print(f"RMQ(0, 49) (Expected 51): {large_sparse_table.range_min_query(0, 49)}")

    # Test Case 6: Array with repeated elements
    print("\nTest Case 6: Array with repeated elements")
    repeated_arr = [4, 4, 4, 4, 4, 4, 4, 4]
    repeated_sparse_table = SparseTable(repeated_arr)
    print(f"RMQ(0, 7) (Expected 4): {repeated_sparse_table.range_min_query(0, 7)}")
    print(f"RMQ(3, 5) (Expected 4): {repeated_sparse_table.range_min_query(3, 5)}")
    print(f"RMQ(2, 2) (Expected 4): {repeated_sparse_table.range_min_query(2, 2)}")


if __name__ == "__main__":
    main()
