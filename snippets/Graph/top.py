def get_has_no_incoming_edge(graph):
    # graph 정점의 총 진입간선을 관리하는 counts 변수 만들기 
    counts = [0] * len(graph)
    # graph 진입간선이 있을 때마다 그 정점에 해당하는 count 값을 1씩 증가시키기
    for vertex in range(len(graph)):
        for curr in graph[vertex]:
            if curr == -1: continue
            counts[curr] += 1

    # graph를 돌다가 진입간선이 없는 정점을 찾으면 리턴시키기
    for vertex in range(len(graph)):
        if graph[vertex] == [-1]: continue
        if counts[vertex] == 0:
            counts[vertex] = -1
            return vertex
    return -1

def topological_sorting(graph):
    # 정렬된 정점을 관리하는 result 변수 만들기
    result = []
    # get_has_no_incoming_edge(graph) 함수로 진입간선이 없는 정점을 받아와 result에 push 하기
    for _ in range(len(graph)):
        vertex = get_has_no_incoming_edge(graph)
        result.append(vertex)
        graph[vertex] = [-1]
    # result 리턴하기
    return result

G = [[], [], [3], [1], [0, 1], [0, 2]]
print(topological_sorting(G))
