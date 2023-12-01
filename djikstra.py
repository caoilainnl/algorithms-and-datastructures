import heapq

def dijkstra(graph, source):
    # Initialize the distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Priority queue to process nodes
    priority_queue = [(0, source)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if we have already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Process neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path is found, update the distance and enqueue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}
source = 'A'
result = dijkstra(graph, source)
print(result)