# 재귀함수를 사용하지 않고 DFS 구현
# [1, 3, 8, 7, 5, 6, 2, 4] 가 return 되도록 할 것

# O(N)
def dfs(adjacent, vertex):
    candidates = [vertex]
    visited = []
    while candidates:
        u = candidates.pop()
        visited.append(u)
        for v in adjacent[u]:
            if v not in visited and v not in candidates:
                candidates.append(v)

    return visited

#O(1)
def dfs(adjacent, vertex):
    candidates = [vertex]
    visited = [False]*(len(adjacent)+1)
    while candidates:
        u = candidates.pop()
        print(u, end=' ')
        for v in adjacent[u]:
            if not visited[v]:
                visited[v] = True
                candidates.append(v)
    return visited

graph = {1:[2,3], 2:[3,4,5], 3:[5,7,8], 4:[5], 5:[6], 6:[], 7:[8], 8:[]}
v = int(input('1부터 8까지의 노드를 선택해서 입력하세용 : '))
dfs(graph, v)
print()
print(dfs(graph, v))
