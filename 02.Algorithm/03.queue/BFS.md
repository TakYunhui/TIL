# BFS
- 너비 우선 탐색, 그래프를 탐색하는 방법
- 탐색 시작점의 인접 정점들을 먼저 모두 차례로 방문한 후, 방문했던 정점을 시작점으로 하여 다시 인접 정점들을 차례로 방문하는 방식
- 인접한 정점들을 탐색한 후, 차례로 다시 너비우선탐색을 진행해야 하므로 선입선출 자료구조인 큐를 활용

```py
def bfs(g, v): # 그래프 g, 탐색 시작점 v
  visited = [0] * (n+1) # n: 정점 개수
  queue = []            # 큐 생성
  queue.append(v)       # 시작점 v를 큐에 삽입
  while queue:          # 큐가 비어있지 않으면
    t = queue.pop(0)    # 큐의 첫번째 원소 반환
    if not visited[t]:  # 방문되지 않은 곳이라면
      visited[t] = True # 방문 표시
      visited(t)        # 정점 t에서 할 일
      for i in g[t]:    # t와 연결된 모든 정점에 대해
        if not visited[i]:  # 방문되지 않은 곳이면
          queue.append(i)   # 큐에 넣기
```
