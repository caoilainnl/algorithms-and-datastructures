class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None

def main():
    # Test case 1: Insert elements into the heap
    print("Test Case 1: Insert Elements")
    heap = MinHeap()
    elements = [10, 4, 15, 20, 0, 8]
    for element in elements:
        heap.insert(element)
        print(f"Inserted {element}, Heap: {heap.heap}")

    expected_heap = [0, 4, 8, 20, 10, 15]
    print("Final Heap: ", heap.heap)
    assert heap.heap == expected_heap, "Heap structure after inserts is incorrect."

    # Test case 2: Extract minimum
    print("\nTest Case 2: Extract Minimum")
    extracted = []
    while heap.get_min() is not None:
        min_val = heap.extract_min()
        extracted.append(min_val)
        print(f"Extracted {min_val}, Heap: {heap.heap}")

    expected_extracted = [0, 4, 8, 10, 15, 20]
    print("Extracted Elements: ", extracted)
    assert extracted == expected_extracted, "Extracted elements order is incorrect."

    # Test case 3: Extract from an empty heap
    print("\nTest Case 3: Extract from Empty Heap")
    empty_extract = heap.extract_min()
    assert empty_extract is None, "Extracting from an empty heap should return None."
    print("Extract from empty heap passed.")

    # Test case 4: Get minimum from an empty heap
    print("\nTest Case 4: Get Minimum from Empty Heap")
    empty_min = heap.get_min()
    assert empty_min is None, "Getting minimum from an empty heap should return None."
    print("Get minimum from empty heap passed.")

    print("\nAll test cases passed!")

if __name__ == "__main__":
    main()
