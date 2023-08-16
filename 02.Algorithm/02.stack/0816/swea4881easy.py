import sys
sys.stdin = open('sample.txt')
T = int(input())

def search(now, acc):
    global result
    # 가지치기는 똑같이 진행
    # 내 누적값이 최종 결괏값보다 한 번이라도 커지면 더 이상 조사 x
    if acc > result:
        return
    # 언제까지 조사 하는가? -> now 가 N이 되면 모든 열에 대한 탐색이 끝났다 가정
    if now == N:
        if acc < result:
            result = acc
    else:
        # 현재 열(now)에서 가능한 모든 행(row)를 탐색
        for row in range(N):
            # 아직 방문한 적 없다면,
            if visited[row] == 0:
                visited[row] = 1 # 현재 행 값 쓰겠다.
                search(now + 1, acc + arr[now][row])
                visited[row] = 0 # 내가 안 쓰고 다음으로 넘겼을 때의 경우

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    '''
    [
        [2, 1, 2], 
        [5, 8, 5], 
        [7, 2, 2]
    ]
    '''
    # 최종 결괏값
    result = 10 * N  # 각 행, 열에서 값 하나씩 구해서 더한 값중 최솟값
    visited = [0] * N # 행의 방문 여부를 저장하는 리스트
    # 시작점, 누적값
    search(0, 0)

    print(f'#{tc} {result}')