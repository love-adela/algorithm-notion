def gvhnie(graph):
    counts = [0] * (len(graph))
    for v in range(len(graph)):
        for u in graph[v]:
            if u == -1: continue
            counts[u] += 1
    for v in range(len(graph)):
        if graph[v] == [-1]: continue
        if counts[v] == 0:
            counts[v] = -1
            return v
    return -1


def topological_sort(graph):
    result = []
    for _ in range(len(graph)):
        v = gvhnie(graph)
        result.append(v)
        graph[v] = [-1]
    return result


G = [[], [], [3], [1], [0, 1], [0, 2]]
print(topological_sort(G))
