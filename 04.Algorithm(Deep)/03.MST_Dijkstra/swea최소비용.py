from collections import deque
def bfs():
    q = deque()
    # x, y 삽입 : 시작좌표는 항상 0, 0
    q.append((0, 0))
    visited[0][0] = 0

    while q:
        x, y = q.popleft()
        # 4방향 조사
        for i in [(0, 1), (1, 0), (-1, 0),  (0, -1)]:
            nx = x + i[0]
            ny = y + i[1]
            # 다음 좌표가 범위 내에 있고, 목적지 좌표의 방문 표시값보다 작거나 같은 경우
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] <= visited[n-1][n-1]:
                # 분기 : 현재 위치가 다음 위치보다 낮거나 높은 것
                if arr[x][y] >= arr[nx][ny]:
                    # 기본 비용만 소모
                    # 다음 칸의 방문 표시값을 현재 표시값이랑 비교
                    if visited[nx][ny] > visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                else:
                    # 높이 차에 대한 비용도 함께 소모
                    if visited[nx][ny] > visited[x][y] + 1 + (arr[nx][ny] - arr[x][y]):
                        visited[nx][ny] = visited[x][y] + 1 + (arr[nx][ny] - arr[x][y])
                        q.append((nx, ny))
t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 가로, 세로 칸 수
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 비교대상
    max_val = sum(sum(arr, [])) + n ** 2
    # 이전에 방문한 적이 있다면 가중치를 visited에 기록할 것
    # => 최초 방문시에도 비교할 수 있는 값이어야 한다
    # 최소 비용을 찾고 있으므로 . . .
    visited = [[max_val] * n for _ in range(n)]
    bfs()
    result = visited[n-1][n-1]

    print(f'#{tc} {result}')