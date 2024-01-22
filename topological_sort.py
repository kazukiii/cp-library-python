def topological_sort_util(v, visited, stack, adjacency_list):
    visited[v] = True
    for i in adjacency_list[v]:
        if not visited[i]:
            topological_sort_util(i, visited, stack, adjacency_list)
    stack.append(v)


def topological_sort(adjacency_list):
    num_vertices = len(adjacency_list)
    visited = [False] * num_vertices
    stack = []

    for i in range(num_vertices):
        if not visited[i]:
            topological_sort_util(i, visited, stack, adjacency_list)

    stack.reverse()
    return stack


if __name__ == "__main__":
    graph = [
        [1, 2],
        [3, 4],
        [4],
        [],
        [],
    ]
    sorted_nodes = topological_sort(graph)
    print(sorted_nodes)  # [0, 2, 1, 4, 3]
