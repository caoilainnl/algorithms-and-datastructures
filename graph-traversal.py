from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # Undirected graph

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        traversal = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                queue.extend(neighbor for neighbor in self.adjacency_list[node] if neighbor not in visited)

        return traversal

    def dfs(self, start):
        visited = set()
        traversal = []
        self._dfs_recursive(start, visited, traversal)
        return traversal

    def _dfs_recursive(self, node, visited, traversal):
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in self.adjacency_list[node]:
                self._dfs_recursive(neighbor, visited, traversal)

def main():
    # Create a graph instance
    graph = Graph()

    # Add edges to the graph
    edges = [
        (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)
    ]
    for u, v in edges:
        graph.add_edge(u, v)

    # Test case 1: BFS Traversal
    print("Test Case 1: BFS Traversal")
    bfs_result = graph.bfs(1)
    expected_bfs = [1, 2, 3, 4, 5, 6, 7]
    print("BFS Result:  ", bfs_result)
    print("Expected BFS:", expected_bfs)
    assert bfs_result == expected_bfs, "BFS traversal does not match expected output."

    # Test case 2: DFS Traversal
    print("\nTest Case 2: DFS Traversal")
    dfs_result = graph.dfs(1)
    expected_dfs = [1, 2, 4, 5, 3, 6, 7]  # One possible valid DFS result
    print("DFS Result:  ", dfs_result)
    print("Expected DFS:", expected_dfs)
    assert dfs_result == expected_dfs, "DFS traversal does not match expected output."

    # Test case 3: Empty Graph Traversal
    print("\nTest Case 3: Empty Graph Traversal")
    empty_graph = Graph()
    assert empty_graph.bfs(1) == [], "BFS on empty graph should return an empty list."
    assert empty_graph.dfs(1) == [], "DFS on empty graph should return an empty list."

    print("\nAll test cases passed!")

if __name__ == "__main__":
    main()
