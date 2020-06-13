# Minimum Spanning Trees (최소 신장 트리)

## Intro

이 문서에서는 Minimum Spanning Trees를 소개한다.
먼저 스패닝 트리(spanning tree)가 무엇인지 알아볼 것이다. 그리고 나서 MST가 최소한의 조건(가중치의 합이 최소가 되는 조건)을 만족시키는 자료구조로서 해당 그래프의 tree에 속한다는 사실을 확인하고 직접 구현해보려고 한다.

## Spanning Tree (신장 트리)

모든 정점 간에 간선이 존재하는 **연결 그래프(Connected Graph)**는 경우에 따라 cyclic 할 수도 있고, acyclic 할 수도 있다. 따라서 우리는 그래프의 일부 간선을 선택해서 acyclic graph인 자료구조로 확장할 수 있다. 이 자료구조의 이름은 스패닝 트리(Spanning Tree)라고 한다.
사이클이 없는 그래프의 일종인 스패닝 트리는 **n**개의 정점과 **n-1**개의 간선을 포함한다. n개의 정점이 있는 그래프에 n-1개 이상의 간선이 존재하면 반드시 사이클이 생기기 때문이다.

## Minimum Spanning Tree (최소신장트리)

MST는 (undirected)그래프 G의 정점들과 간선들로 구성된 여러 개의 스패닝 트리 중 간선의 가중치의 합이 최소인 트리다. Spanning tree의 모든 edge에 weight가 있다면, spanning tree는 여러개 발생한다. MST를 찾는다는 의미는 한 그래프에서 발생할 수 있는 여러 spanning tree 중에서 특별한 조건에 해당하는 spanning tree를 선택하는 뜻이다.

스패닝트리에서 *spanning*이라는 단어는 뻗는다는 의미를 지니므로, MST를 만드는 목적은 그래프 G의 간선의 가중치의 합이 최소가 되는 Tree를 찾는 것이라고 기억하면 좋을 것 같다.

## Prim Algorithm

눈 앞의 이익만 추구하는 greedy algorithm의 일종으로, 알고리즘 과정 중간의 한 시점에 관해 귀납적으로 설명할 수 있다는 특징이 있다. Prim alogirthm은 greedy algorithm으로 최적해를 보장하는 드문 예다.

### Algorithm

        Prim(G, r)
        {
            S ← ∅;
            정점 r에 방문되었다고 표시하고, 집합 S에 포함시킨다.;
            while (S V) {
                S에서 V-S를 연결하는 간선들 중 최소길이의 간선 (x, y)를 찾는다;
                정점 y를 방문되었다고 표시하고, 집합 S에 포함시킨다.
                (정점 y로 relaxation 할 수 있으면 한다.)
            }
        }


알고리즘 첫번째 단계에서는 singleton set, 즉 vertex 한 개 또는 공집합을 집합 S에 포함시킨다.
이후 단계별로 집합 S에 원소를 하나씩 늘릴 수 있고 알고리즘을 종료할 수도 있다.
중간 단계의 한 시점을 살펴보자. 현재 집합 S의 원소는 Spanning tree에 연결된 vertex로 결정된다. 즉, 집합 S의 subset으로 spanning tree를 만들 수 있게 되는 셈이다. 이때의 spanning tree로 구성된 집합 S 외부의 vertex와 연결되는 edge 중, 연결 cost가 가장 적은 edge를 찾는다. 이 edge와 연결된 vertex를 집합 S에 새로 포함시킨다. 이로써 Spanning tree가 또 한 번 확장된다.

### 특징

vertex의 총 개수를 n개라고 할 때, 하나의 edge를 통해서 vertex로 연결시키는 과정을 n-1번 하면, 모든 vertex가 연결된 spanning tree가 된다. 즉, acyclic connected graph를 만들기 위해서는 n-1개의 edge가 필요하다. 집합 S 바깥에서 안으로 vertex가 추가되기 때문에(해당 그래프로부터 spanning시키기 때문에), 절대로 cycle이 생기지 않게되므로 이 자료구조는 spanning tree 조건에 들어맞게 된다.

* 시간복잡도 : O(ElogV)

### Code



## Kruthkal Algorithm