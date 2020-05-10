백준 오프라인 강의와 강의자료를 참고했음을 미리 밝힙니다.

# 그래프의 탐색

* 목적: 임의의 시작점 x로부터 시작해서 모든 정점을 한 번씩 방문하기 위해서.

* 종류: 어떤 순서로 가느냐에 따라서 달라짐.
  * DFS(Depth First Search)
    * 갈 수 있는데까지 계속 진행하다가 더이상 진행할 수 없으면 뒤로 돌아오고 다시 진행하는 알고리즘
  * BFS(Breadth First Search)
    * 한 정점에서 갈 수 있는 곳을 동시에 가는 알고리즘

## 1. DFS

스택이 현재까지 어떤 정점을 들렸는지를 다 기록하고 있기 때문에, 최대한 많이 움직이다가 더이상 갈 수 없으면 이전 정점으로 돌아온다. 이전 정점에서 갈 수 있는 다른 정점으로 다시 움직이는 알고리즘.
탐색 종료 시점은 더이상 갈 수 있는 정점이 없어서 이전 정점으로 재귀적으로 돌아가면서 더이상 방문할 정점이 없는 때를 의미한다.

### 1.1 구현

#### 1.1.1 인접행렬로 구현

```
// adjacent matrix in c++
void dfs(int x) { // dfs(x)는 정점 x에 방문했다라는 것을 의미
    check[x] = true;
    printf("%d ", x);
    for (int i=1; i<=n; i++) { // 인접행렬로 구현, n은 차수
        if (a[x][i] == 1 && !check[i]) {  // **간선이 존재** && 방문하지 않았을 때
            dfs(i);
        }
    }
}
```

```
# adjacent matrix in python
def dfs(x):
    check[x] = True
    print(x, end=' ')
    for i in check[x]:
        if not check[i]:
            dfs(i)
```

#### 1.1.2 인접리스트로 구현

인접행렬과 저장방식만 다르다. 다음 정점, 즉 간선을 나타내는 코드만 다르다.

```
// adjacent list in c++
void dfs(int x) {
    check[x] = true;
    printf("%d ", x);
    for (int i=0; i<a[x].size(); i++) { // x에 있는 정점의 개수만큼 반복
        int y = a[x][i]; // 간선에 연결된 다음 정점을 찾는다.
        if (!check[y]) { // 방문하지 않았으면 (간선이 존재하는지 체크하지 않아도 됨)
            dfs(y); // dfs() 를 재귀호출
        }
    }
}
```

### 1.2 시간복잡도

dfs(x)는 x에 방문하는 함수이므로 정점의 개수, 즉 차수인 V번만큼 dfs(x)가 호출된다.
따라서 dfs(x) 시간복잡도 * v가 전체 dfs 알고리즘의 시간복잡도가 된다.

* 인접행렬
  * 모든 정점을 다 찾아봐야 하기 때문에 dfs(x)의 시간 복잡도는 O(V)가 된다.
  * dfs(x)가 V번 호출되어야 하므로 전체 dfs 알고리즘의 시간복잡도는 O(V*V) = O(V^2)
* 인접리스트
  * 인접행렬과 마찬가지로 dfs(x)는 v번 호출된다.
  * dfs(x)의 시간복잡도는 O(V+E)
    * 인접리스트에서 dfs가 호출되는 방법은 모든 정점을 다 찾는 인접행렬의 탐색 방법과 다르다.
    * 또한 `a[x].size()`는 전체 간선의 개수가 아니라, 한 정점과 연결된 간선의 개수이기 때문에 dfs(x)의 시간복잡도는 O(E)가 아님을 주의해야 한다.

## 2. BFS

BFS 알고리즘은 Queue를 이용해서 어디를 방문할 것인지를 기록한다.
BFS에서는 갈 수 있는 모든 정점을 일단 Queue에 넣는다. Queue에 넣는 행위는 '방문했다'라는 것을 의미한다.
방문했다는 것을 의미하는 check[i]를 변경하는 시점은 queue에 넣을 정점을 때다. queue에 넣어놓고 check[i]를 변경시키지 않으면 방문한 정점이 queue에 중복되어 생기기 때문이다. 이는 모든 정점을 한 번씩 방문하겠다는 그래프의 탐색 목적에 위배된다.  

queue가 비어있으면 BFS 탐색을 완료한다.

### 2.1 구현

#### 2.1.1 인접행렬로 구현

C++는 queue<int> 같은 stl을 사용, Java는 Queue<Integer>, Python은 collections.deque()를 사용한다. 또는 직접 구현해도 무방.

```
// adjacent matrix in c++
queue<int> q;
check[1] = true; q.push(1); // 시작점을 1이라고 가정한다.
while (!q.empty()) {
    int x = q.front(); q.pop(); // queue의 가장 앞에 있는 것을 빼준다. x는 현재 내가 방문하고 있는 정점을 의미한다. 
    printf("%d ", x);
    for (int i =1; i<=n; i++) { // 인접행렬에서는 1부터 정점 개수 n만큼 모두 살펴보아야 한다. 
        if (a[x][i] == 1 && !check[1]) { // 간선이 있고 아직 방문하지 않았다면,
            check[i] = true; // 방문과 동시에 queue에 중복된 정점이 생기는걸 막기 위해 check배열을 갱신한다.
            q.push(i);
        }
    }
}
```

#### 2.1.2 인접리스트로 구현

다음 정점을 찾는 방법이 달라진다.

```
// adjacent list in c++
queue<int> q;
check[1] = true; q.push(1);
while (!q.empty()) {
    int x = q.front(); q.pop();
    printf("%d ", x);
    for (int i=0; i<a[x].size(); i++;) {
        int y = a[x][i];
        if (check[y] == false) {
            cehck[y] = true; q.push(y);
        }
    }
}
```

### 2.2 시간복잡도

dfs()의 시간복잡도와 같다.

* 인접행렬 : O(V^2)
* 인접리스트 : O(V+E)
  * `if (check[y]== false)` 검사를 하기 때문에 모든 정점을 다 방문하는게 아니라, 간선의 개수 (V)에다가 정점의 개수(E)만큼이 추가되는 것을 의미한다.