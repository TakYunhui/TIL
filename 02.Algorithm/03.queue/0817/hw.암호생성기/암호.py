# 큐 이용
from collections import deque
for tc in range(10):
    tc = int(input())
    q = deque((list(map(int, input().split()))))
    while True:
        # 마지막 숫자가 0이면 종료
        if q[-1] == 0:
            break
        else:
            for i in range(1, 6):
                if q[0] - i > 0:
                    q.append(q.popleft()-i)
                else:
                    q[0] = 0
                    q.append(q.popleft())
                    break
    print(f'#{tc}', *q)

