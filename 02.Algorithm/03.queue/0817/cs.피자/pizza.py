from collections import deque
t = int(input())
for tc in range(1, t +1):
    # n: 화덕크기 m: 피자개수
    n, m = map(int, input().split())
    # 피자별 치즈양
    c = list(map(int, input().split()))
    # 피자 번호
    nums = [i+1 for i in range(m)]

    q = deque()  # 치즈가 들어감
    q2 = deque() # 피자 번호가 들어감
    # 화덕이 수용 가능한 수만큼 피자 돌릴 것
    # 피자 번호도 같은 과정을 거친다
    for _ in range(n):
        q.append(c.pop(0))
        q2.append(nums.pop(0))
    # print(q)
    while True:
        if len(q) == 1: # 화덕에 피자가 1개만 남게 된다면 작업 종료
            break
        # 피자 구워서 치즈 녹이는 과정
        # 맨 앞의 피자를 녹여서(//2) 뒤로 이동시키면 한 바퀴 회전하며 치즈 녹이는 것과 같다
        q.append(q.popleft()//2)
        # 피자에 맞는 번호도 주어야 하므로 번호 큐도 같은 과정을 거친다, 이때 번호는 그대로이므로 연산자 x
        q2.append(q2.popleft())
        # print(q)

        # 만약 치즈가 다 녹은 피자가 생겼다면 화덕에서 빼고, 남아있는 피자를 그 자리에 넣는다
        if q[-1] == 0 and c:
            q.pop()
            q2.pop()
            q.append(c.pop(0))
            q2.append(nums.pop(0))
            # print(q)

        # 추가로 넣을 피자가 없다면 치즈가 다 녹은 피자들은 화덕에서 제거해준다
        elif q[0] == 0 or q[-1] == 0:
            q.pop()
            q2.pop()
    # 화덕에 남아있는 피자 '번호' 출력
    print(f'#{tc}', *q2)

