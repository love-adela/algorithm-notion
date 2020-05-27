"""
* adjacent : 입력으로 주어지는 그래프 `dict`
* start : 시작정점 `int`
* candidates: 방문해야 할 정점 `queue`
* start: 방문한 정점 `list`
bfs 결과는 [1, 2, 3, 4, 5, 7, 8, 6]이 되어야 함
"""
from collections import deque
def bfs(adjacent:dict, start:int)-> list:
    lst = []
    candidates = deque([start])
    was_candidate = [False] * (len(adjacent)+1)
    was_candidate[start] = True
    while candidates:
        curr = candidates.popleft()
        for vertex in adjacent[curr]:
            if not was_candidate[vertex]:
                was_candidate[vertex] = True
                candidates.append(vertex)
        lst.append(curr)
    return lst

graph = {1:[2,3], 2:[3,4,5], 3:[5,7,8], 4:[5], 5:[6],       6:[], 7:[8], 8:[]}
print(bfs(graph, 1))
