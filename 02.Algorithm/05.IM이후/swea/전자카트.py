# 정지헌[부울경_임시1반] 님이 이 세션에 있는 모든 사람에게:    오후 4:22
def recursive(depth, start, total):
    global rlt
    if depth == N:
        rlt = min(rlt, box[start][0] + total)
        return
    for i in range(1, N):
        if not visited[i] and start != i:
            visited[i] = 1
            recursive(depth+1, i, total + box[start][i])
            visited[i] = 0

T = int(input())
for t in range(T):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    rlt = float('inf')
    recursive(1, 0, 0)
    print(f'#{t+1}', rlt)