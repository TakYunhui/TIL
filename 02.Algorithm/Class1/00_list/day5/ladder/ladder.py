# ladder
# 그림으로 표시되는 예시는 축소된 범위
# input 데이터 읽어오기
import sys
sys.stdin = open('input.txt')
    # 1. 아래로 조사를 진행함
    # 2. 단, 좌-우 중 갈 수 있는 곳을 마주하면 그쪽으로 먼저 갈 것
    # 3. 이미 지나온 길은 다시 돌아가지 않아야 함
    # 4. 마지막 행(99, n)이 되었을 때에는 종료
    # 5. 마지막 행에서 마주한 값이 2인 경우, 출발 좌표 출력
    # 6. 위 모든 과정을 모든 출발점에 대해서 실행해야 함

    # 하, 좌, 우
dx = [1, 0, 0]
dy = [0, -1, 1]
# 필요 인자: 시작 좌표 (x, y)
def search(x, y):
    #
    visited = [[0] * ]
    # 만약 2를 찾았을 때, 반환해야 할 시작 좌표 y를 기록
    original_y = y

    # 방문 표시
    visited[x][y] = 1
    # 조사 조건은 x가 99가 되기 전까지
    while x != 99:
        # 계속 아래로 조사하면서 진행
        # 조사 순서는? 하, 좌 우? 하, 우 좌?
        for k in range(3):
             # 다음 조사 위치 좌표
             # 다음 지역 x, y 좌표 | 현재 위치 x, y 좌표 + 다음 방향에 대한 좌표
             nx = x + dx[k]
             ny = y + dy[k]
        # 다음 조사를 할 예정지인 (nx, ny) 위치가 안전하게 조사 가능한지
        # 조건으로 확인
        # 다음 조사 가능 여부 조건에 data[nx][ny] == 1
        if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny] != 0 and visited[nx][ny] == 0:
            x, y = nx, ny
            # 이전에 있던 위치를 0으로 바꿔버리면 어떨거?
            # 다른 경우의 수에 영향을 미쳐서 안되더라
            # data[x][y] = 0
            # 새롭게 방문한 장소 방문 표시
    # x가 99가 된 순간
    if data[x][y] == 2:
        return original_y
    else:
        return '실패'






# 테스트 케이스 10개
# tc 임시 변수는 최후 출력값에서 tc번호 표기할 때 사용해서 1~10
for _ in range(10):
    tc = int(input())
    # 100 * 100의 2차원 리스트
    data = [list(map(int, input().split())) for _ in range(100)]

    # 모든 출발점 찾기
    for i in range(100):
        # 항상 0번째 열에서 출발 -> 이중 포문 필요 x
        # 0번째 열의 i번째 행의 값이 1이면
        if data[0][i] == 1:
            #  print(i)        # 모든 출발점
            result = search(0, i) # 코드 실행 결과 반환
        if result != '실패': # 조사를 한번 끝냈는데, result에 '실패'말고 다른 게 있다?
        # 값을 찾았으니 종료
            break
    print(f'#{tc} {result}')

