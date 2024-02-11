class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def range_update(self, l, r, value):
        self._range_update(0, 0, self.n - 1, l, r, value)

    def _range_update(self, node, start, end, l, r, value):
        # Handle any pending updates
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:  # Propagate laziness to children
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0

        # No overlap
        if start > r or end < l:
            return

        # Total overlap
        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * value
            if start != end:  # Propagate laziness to children
                self.lazy[2 * node + 1] += value
                self.lazy[2 * node + 2] += value
            return

        # Partial overlap
        mid = (start + end) // 2
        self._range_update(2 * node + 1, start, mid, l, r, value)
        self._range_update(2 * node + 2, mid + 1, end, l, r, value)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def range_query(self, l, r):
        return self._range_query(0, 0, self.n - 1, l, r)

    def _range_query(self, node, start, end, l, r):
        # Handle any pending updates
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:  # Propagate laziness to children
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0

        # No overlap
        if start > r or end < l:
            return 0

        # Total overlap
        if start >= l and end <= r:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_query = self._range_query(2 * node + 1, start, mid, l, r)
        right_query = self._range_query(2 * node + 2, mid + 1, end, l, r)
        return left_query + right_query


# Testing the implementation
def main():
    print("Running exhaustive tests for Segment Tree with Lazy Propagation...")

    # Test Case 1: Basic range update and query
    print("\nTest Case 1: Basic range update and query")
    arr = [1, 2, 3, 4, 5]
    seg_tree = SegmentTree(arr)
    seg_tree.range_update(1, 3, 2)
    print(f"Range Query (1, 3) (Expected 17): {seg_tree.range_query(1, 3)}")
    print(f"Range Query (0, 4) (Expected 19): {seg_tree.range_query(0, 4)}")

    # Test Case 2: Non-overlapping range update
    print("\nTest Case 2: Non-overlapping range update")
    seg_tree.range_update(0, 0, 5)
    seg_tree.range_update(4, 4, 10)
    print(f"Range Query (0, 0) (Expected 6): {seg_tree.range_query(0, 0)}")
    print(f"Range Query (4, 4) (Expected 15): {seg_tree.range_query(4, 4)}")

    # Test Case 3: Overlapping range updates
    print("\nTest Case 3: Overlapping range updates")
    seg_tree.range_update(2, 4, 3)
    print(f"Range Query (2, 4) (Expected 31): {seg_tree.range_query(2, 4)}")
    print(f"Range Query (0, 2) (Expected 17): {seg_tree.range_query(0, 2)}")

    # Test Case 4: Full array range update
    print("\nTest Case 4: Full array range update")
    seg_tree.range_update(0, 4, 1)
    print(f"Range Query (0, 4) (Expected 35): {seg_tree.range_query(0, 4)}")
    print(f"Range Query (3, 3) (Expected 8): {seg_tree.range_query(3, 3)}")

    # Test Case 5: Edge case with single-element array
    print("\nTest Case 5: Edge case with single-element array")
    single_arr = [10]
    single_tree = SegmentTree(single_arr)
    single_tree.range_update(0, 0, 5)
    print(f"Range Query (0, 0) (Expected 15): {single_tree.range_query(0, 0)}")

    # Test Case 6: Large range and values
    print("\nTest Case 6: Large range and values")
    large_arr = [i for i in range(1, 1001)]
    large_tree = SegmentTree(large_arr)
    large_tree.range_update(0, 999, 10)
    print(f"Range Query (0, 999) (Expected 505500 + 10000): {large_tree.range_query(0, 999)}")
    print(f"Range Query (500, 750) (Expected 93776): {large_tree.range_query(500, 750)}")


if __name__ == "__main__":
    main()
