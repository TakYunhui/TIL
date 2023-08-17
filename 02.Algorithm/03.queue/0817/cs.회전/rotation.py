from collections import deque
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    # m번 작업
    for i in range(m):
        q.append(q.popleft())
    print(f'#{tc} {q[0]}')