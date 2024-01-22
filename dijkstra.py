import heapq


def dijkstra(graph, start):
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = [
        [(1, 2), (2, 5)],
        [(2, 1), (3, 2)],
        [(3, 5)],
        [],
    ]
    start_node = 0
    distances = dijkstra(graph, start_node)
    # the shortest distances from the start node to each node -> [0, 2, 3, 4]
    print(distances)
