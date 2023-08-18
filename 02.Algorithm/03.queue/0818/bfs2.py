# 연습문제 3
'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''
def bfs(s, v): # 시작 정점 s, 마지막 정점 v
    visited = [0] * (v+1)   # visited 생성
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    
    while q:        # 큐에 정점이 남아있으면 (front != rear)
        t = q.pop(0) # 디큐
        print(t)     # 방문한 정점에서 할 일 
        for w in range(1, v+1):         # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if adj_m[t][w] == 1 and visited[w] == 0:
                q.append(w)        # w 인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1

v, e = map(int, input().split()) # 1번부터 v번 정점, e개의 간선
arr = list(map(int, input().split()))
# 인접 행렬 -------------------------
adj_m = [[0] * (v+1) for _ in range(v+1)]
for i in range(e):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1     # 방향이 없는 경우
# 여기까지 인접행렬 ------------------
bfs(1, v)