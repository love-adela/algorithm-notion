from collections import deque
def bfs(adjacent, vertex):
    q = deque([vertex])
    distance = [-1]*len(adjacent)
    distance[v] = 0
    while q:
        p = q.popleft()
        for q in adjacen[p]:
            if distance[q]






# O(V+E)
BST = [
    0,
    [1, [2, None, None], [3, None, None]],
    [4, None, [5, None, None]],
] # Tree

# Queue 쓰기
def bfs(tree: tuple) -> None:    
    queue = [tree]    
    while queue: # list가 비어있을 때까지 돌아간다. 즉, while True와 같은 표현
        node = queue.pop(0)
        value, left, right = node # unpacking
        print(value)
        if left is not None:
            queue.append(left)
        if right is not None:
            queue.append(right)

# Test
bfs(BST)
