# N * N 미로
# 출발지 -> 목적지
# 최소 몇 개의 칸?
def bfs(sti, stj, n):
    visited = [[0]*n for _ in range(n)] # visited 생성
    q = []                 # 큐 생성
    q.append((sti, stj))   # 시작점 인큐
    visited[sti][stj] = 1  # 시작점 인큐 표시
    while q:               # 큐가 비워질 때 까지
        i, j = q.pop(0)    # 디큐
        if maze[i][j] == 3:# 처리
            return visited[i][j] - 2 # 지나온 칸 수 리턴
        # 인접하고 인큐된 적이 없으면 . . .
        # 인큐, 인큐 표시
        for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
            ni, nj = i + di, j + dj
            # maze 가 벽이 아니면
            if 0<=ni<n and 0<=nj<n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0    # 3인 칸에 도달할 수 없는 경우

def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2: # 시작점 2
                return i, j

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 미로 크기
    maze = [list(map(int, input())) for _ in range(n)]
    sti, stj = find_start(n) # 시작점 찾기
    ans = bfs(sti, stj, n)   # 거리 알아내기
    print(f'#{tc} {ans}')