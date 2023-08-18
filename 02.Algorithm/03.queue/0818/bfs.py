# 연습문제 3
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, v): # 시작 정점 s, 마지막 정점 v
    visited = [0] * (v+1)   # visited 생성
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    
    while q:        # 큐에 정점이 남아있으면 (front != rear)
        t = q.pop(0) # 디큐
        print(t)     # 방문한 정점에서 할 일 

        for w in adj_l[t]:         # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)        # w 인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1


v, e = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)
# 인접 리스트 -------------------------
adj_l = [[] for _ in range(v+1)]
for i in range(e):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)          # 방향이 없는 경우
# 여기까지 인접리스트 ------------------
# print(adj_l)
'''
[[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
'''
bfs(1, v)