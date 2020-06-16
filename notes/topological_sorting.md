# Topological Sorting

## Concept

edge (i, j)가 존재하면 작업 i는 반드시 작업 j보다 먼저 수행된다. 그림의 모든 간선에 대해서 이 성질만 만족하면 어떤 순서라도 좋다. 이러한 성질을 만족하는 정렬을 위상정렬이라고 한다. 

* 정점 u의 진입간선 : u에 연결된 간선 중 u로 향하는 간선 
* 정점 u의 진출간선 : u에 연결된 간선 중 u로 나가는 간선

## Characterisitcs

* Used for Job scheduling
* Very fast, Linear time
* When we are given directed acyclic graph(DAG), I want to order vertices so that all edges point from lower order to higher order.
* Imagine when you dress up, there's no cycles because then you can't get dressed.
* There could be some unrelated vertecies in the graph which you could think of as a topology.

How we do topological sort?

* Run DFS output reverse of finishing times of vertices. Everytime I finish a vertex, I could add it to a list. I take that order and I reverse it. That would be a topological order.

Why does it run?

* Assume there are no back edges in DAG. So all the edges are tree edges, forward edges, and cross edges. And we use that to prove the theorem.
* We want to prove that all the edges point from an earlier number to a later number.
(무슨 뜻이냐면 간선 uv에서 정점 u이전에 정점 v를 다녀온걸 보이겠다.-> reverse order이라고 하는 이유)
Proof that topological sort gives you a valid job schedule.
There are two possible cases.

Case1: u starts before v [o]

u → v : v is reachable from u, so maybe via this edge, or maybe via some other path, we will eventually visit v in the recursion for u. So before u finishes, we will visit v.

Case2: v starts before u [x: contradiction]

(still) u → v: but now we start at v, u has not yet been visited. Well, now we worry that we visit u. If we visit u, we're going to finish u before we finish v, but we want it to be the other way around. Why can't that happen? Because in particular, the graph would have to be cyclic.
요약 : 작업 i와 작업 j 사이에 간선 (i, j)가 존재한다면 작업 i는 반드시 작업 j보다 먼저 수행된다.
Adela어제 오전 3:19
참고 : course scheduling이라고 부르기도 한다.
Adela어제 오전 3:28
메모 :
- 작업 j보다 먼저 수행되는 i가 무엇인지 아는게 중요한게 아니라 어떤 j가 선행노드(prerequisite)가 있는지 파악하는게 중요함.

* acycle: back edges(x), tree edges(o), forward edges(o), cross edges(o)
  
======================================================================
