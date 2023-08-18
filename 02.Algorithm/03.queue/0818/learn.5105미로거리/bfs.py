import sys
sys.stdin = open('sample_input.txt')
t = int(input())

# bfs로 도착지점 경로 이동 칸 수 구하기
def bfs(sti, stj, n):
    visited = [[0] * n for _ in range(n)]   # 방문 지점
    # -> 1번부터 시작 x, 위치 정보가 (i, j) 형식으로 들어오므로 n * n
    q = [(sti, stj)] # 큐 생성 후 시작지점 인큐
    visited[sti][stj] = 1 # 방문 표시

    while q:
        i, j = q.pop(0) # 디큐
        if maze[i][j] == 3:
            return visited[i][j] - 2 # 이동한 칸(총 칸 수 - 출발, 도착 지점)
        # 델타 탐색 -> 좌우하상 이동
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni = i + di
            nj = j + dj
            # 방향 별 이동한 위치가 미로 범위 안이어고, 벽(1)이 아니고, 방문하지 않았다면!
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))          # (ni, nj) 지점을 인큐
                visited[ni][nj] = visited[i][j] + 1 # 방문여부 누적 + 1 (=> 총 이동 거리 칸수)
    return 0 # 3에 도착하지 못 한다면 0





# 시작지점 위치를 찾는 함수
def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2: # 2일때 시작점!
                return i, j

for tc in range(1, t+1):
    n = int(input()) # 미로 크기
    # 2차원 행렬 미로
    maze = [list(map(int, input())) for _ in range(n)]
    sti, stj = find_start(n)
    print(f'#{tc} {bfs(sti, stj, n)}')

