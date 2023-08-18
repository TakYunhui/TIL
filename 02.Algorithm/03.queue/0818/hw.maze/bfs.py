import sys
sys.stdin = open('input.txt')

def bfs(sti, stj, n):
    visited = [[0] * n for _ in range(n)] # visited 생성
    q = [(sti, stj)]      # 큐 생성 및 시작점 인큐
    visited[sti][stj] = 1 # 시작점 인큐 표시
    while q:              # 큐가 비워질 때까지
        i, j = q.pop(0)   # 디큐 (가장 앞의 값)
        if maze[i][j] == 3: # 도착지점 3에 도달하면
            return 1        # 1 반환
        # 인접 지점이면서 인큐된 적이 없다면
        for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]: # 방향 지정
            ni, nj = i + di, j + dj
            # 다음 위치가 미로 범위 내이고, 벽이 아니면
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj)) # 큐에 해당 지점 인큐
                visited[ni][nj] = visited[i][j] + 1
    return 0 # 목표에 도달할 수 없는 경우 0 반환


def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j

for _ in range(10):
    # 테스트케이스 번호
    tc = int(input())
    # 16 x 16 미로 2차원리스트(행렬)
    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)
    sti, stj = find_start(16)
    print(f'#{tc} {bfs(sti, stj, 16)}')