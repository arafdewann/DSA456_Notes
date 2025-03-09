# Example of Dijkstra's algorithm to find the shortest path in a graph code

import heapq

def dijkstra(graph, start):
    heap = [(0, start)]  # (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)  # Get node with min distance
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distances[neighbor]:  # Found a shorter path
                distances[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return distances

graph = {
    'A': [('B', 2), ('C', 4), ('D', 1)],
    'B': [('D', 7)],
    'C': [('D', 3)],
    'D': [('E', 2)],
    'E': []
}

print(dijkstra(graph, 'A'))

# Output: {'A': 0, 'B': 2, 'C': 4, 'D': 1, 'E': 3}

