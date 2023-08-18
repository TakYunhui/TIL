from collections import deque
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    # 맨 앞의 숫자를 뒤로 옮기는 작업
    # m번 실행
    for i in range(m):
        q.append(q.popleft())
    print(f'#{tc} {q[0]}')