import sys
sys.stdin = open('sample.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최종 결괏값
    result = 10 * N  # 각 행, 열에서 값 하나씩 구해서 더한 값중 최솟값
    visited = [0] * N # 행의 방문 여부를 저장하는 리스트
    # 현재 위치(시작점)와 누적값
    now = 0
    acc = 0
    # stack 에 다음 조사 대상 담음
    # 매번 조사 대상마다 visited는 별개로 처리해서 검사ㅐ야하니
    # 새 리스트로 만들어서 복사
    stack = [(now, acc, visited[:])] # 튜플 하나가 첫 번째 조사 대상 ~
    while stack:
        # 다음 조사 대상
        now, acc, visited = stack.pop()
        if acc > result:
            continue
        # 언제까지 조사 하는가? -> now 가 N이 되면 모든 열에 대한 탐색이 끝났다 가정
        if now == N:
            if acc < result:
                result = acc
        else:
            # 현재 열(now)에서 가능한 모든 행(row)를 탐색
            for row in range(N):
                # 아직 방문한 적 없다면,
                if visited[row] == 0:
                    # visited[row] = 1  # 현재 행 값 쓰겠다.
                    new_visited = visited[:]
                    new_visited[row] = 0  # 내가 안 쓰고 다음으로 넘겼을 때의 경우
                    stack.append((now+1, acc+arr[now][row], new_visited))
    print(f'#{tc} {result}')