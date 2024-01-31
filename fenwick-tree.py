class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_add(self, left, right, value):
        self.add(left, value)
        self.add(right + 1, -value)

    def point_query(self, index):
        return self.sum(index)

class FenwickRangeUpdatePointQuery:
    def __init__(self, size):
        self.size = size
        self.BIT1 = FenwickTree(size)
        self.BIT2 = FenwickTree(size)

    def range_update(self, left, right, value):
        # Update BIT1 and BIT2 to apply the range increment
        self.BIT1.range_add(left, right, value)
        self.BIT2.range_add(left, right, value * (left - 1))
        self.BIT2.range_add(right + 1, self.size, -value * right)

    def point_query(self, index):
        # Calculate the actual value at index using BIT1 and BIT2
        return self.BIT1.sum(index) * index - self.BIT2.sum(index)

# Testing the implementation
def main():
    print("Running exhaustive tests...")
    
    # Test Case 1: Basic functionality
    print("\nTest Case 1: Basic functionality")
    size = 10
    fenwick = FenwickRangeUpdatePointQuery(size)
    fenwick.range_update(2, 5, 10)
    print(f"Point Query 3 (Expected 10): {fenwick.point_query(3)}")
    print(f"Point Query 6 (Expected 0): {fenwick.point_query(6)}")

    # Test Case 2: Multiple overlapping range updates
    print("\nTest Case 2: Multiple overlapping range updates")
    fenwick.range_update(3, 7, 5)
    print(f"Point Query 4 (Expected 15): {fenwick.point_query(4)}")
    print(f"Point Query 6 (Expected 5): {fenwick.point_query(6)}")
    print(f"Point Query 8 (Expected 0): {fenwick.point_query(8)}")

    # Test Case 3: Single point update (range of size 1)
    print("\nTest Case 3: Single point update (range of size 1)")
    fenwick.range_update(4, 4, 7)
    print(f"Point Query 4 (Expected 22): {fenwick.point_query(4)}")
    print(f"Point Query 5 (Expected 15): {fenwick.point_query(5)}")

    # Test Case 4: Large range update
    print("\nTest Case 4: Large range update")
    fenwick.range_update(1, 10, 3)
    print(f"Point Query 1 (Expected 3): {fenwick.point_query(1)}")
    print(f"Point Query 10 (Expected 3): {fenwick.point_query(10)}")
    print(f"Point Query 5 (Expected 18): {fenwick.point_query(5)}")

    # Test Case 5: No updates
    print("\nTest Case 5: No updates")
    new_fenwick = FenwickRangeUpdatePointQuery(size)
    print(f"Point Query 3 (Expected 0): {new_fenwick.point_query(3)}")

    # Test Case 6: Edge cases
    print("\nTest Case 6: Edge cases")
    fenwick.range_update(10, 10, 100)
    print(f"Point Query 10 (Expected 103): {fenwick.point_query(10)}")
    fenwick.range_update(1, 1, 50)
    print(f"Point Query 1 (Expected 53): {fenwick.point_query(1)}")

if __name__ == "__main__":
    main()
