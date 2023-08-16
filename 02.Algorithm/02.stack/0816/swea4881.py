import sys
sys.stdin = open('sample.txt')

def make_candidates(visited, now, c):
    in_perm = [False] * NMAX
    for i in range(1, now):
        in_perm[visited[i]] = True
    ncands = 0
    for i in range(1, N+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands


def backtrack(visited, now, end, acc):
    global result
    # 가지치기   더 이상 유망성 없으니 조사하러 갈 이유가 없다.
    if acc > result:
        return

    c = [0] * MAXCANDIDATES

    # 아직 누적값이 result보다 크지 않아서, 최솟값이 될 가능성이 남아 있다면,
    # 언제까지 조사 할거냐?
    if now == end:  # 그래야 모든 열에 대해 조사가 가능하니까
        # 그래서 지금까지 쌓인 acc가 result보다 작아서
        # 최솟값을 갱신 할 수 있는지 확인
        if acc < result:
            result = acc
    else:
        now += 1
        # 현재 위치의 후보 생성
        ncands = make_candidates(visited, now, c) # 후보군 생성하고, 그 후보군의 길이를 반환
        for i in range(ncands):
            visited[now] = c[i]
            backtrack(visited, now, end, acc + arr[now - 1][visited[now] - 1])
            visited[now] = False


T = int(input())

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
    MAXCANDIDATES = N # 최대 후보군 수
    NMAX = N+1
    visited = [False] * NMAX
    # 방문 표시, 시작점, 끝점, 누적값
    backtrack(visited, 0, N, 0)

