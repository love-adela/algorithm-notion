"""
* adjacent : 입력으로 주어지는 그래프 `dict`
* start : 시작정점 `int`
* candidates: 방문해야 할 정점 `queue`
* start: 방문한 정점 `list`
bfs 결과는 [1, 2, 3, 4, 5, 7, 8, 6]이 되어야 함
"""
# from collections import deque
# def bfs(adjacent:dict, start:int)-> list:
#    lst = []
#    candidates = deque([start])
#    was_candidate = [False] * (len(adjacent)+1)
#    was_candidate[start] = True
#    while candidates:
#        curr = candidates.popleft()
#        for vertex in adjacent[curr]:
#            if not was_candidate[vertex]:
#                was_candidate[vertex] = True
#                candidates.append(vertex)
#        lst.append(curr)
#    return lst


def bfs(adjacent, vertex):
    candidates = [vertex]
    visited = [False] * (len(adjacent) + 1)

    while candidates:
        curr, *candidates = candidates
        print(curr, end=' ')
        for node in adjacent[curr]:
            if not visited[node]:
                visited[node] = True
                candidates.append(node)
    return visited


graph = {1: [2, 3],
         2: [3, 4, 5],
         3: [5, 7, 8],
         4: [5],
         5: [6],
         6: [],
         7: [8],
         8: []}
start = int(input('1부터 8까지의 노드 중 하나를 고르세용: '))
bfs(graph, start)
