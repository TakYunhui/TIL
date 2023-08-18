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
            # 한 사이클 -> 5번 작업
            # 첫 번째 수를 1 감소시켜 맨 뒤로
            # 그 다음 첫 번째 수를 2 감소시켜 맨 뒤로 ...
            # 1, 2, 3, 4, 5 순으로 뺀다
            for i in range(1, 6):
                if q[0] - i > 0:
                    q.append(q.popleft()-i)
                # 만약 계산한 값이 0보다 작거나 같다면
                else:
                    # 해당 값을 0으로 바꿔서 맨 뒤로 보내면 ... 
                    # 비밀번호 생성 완료
                    q[0] = 0
                    q.append(q.popleft())
                    break
    print(f'#{tc}', *q)

