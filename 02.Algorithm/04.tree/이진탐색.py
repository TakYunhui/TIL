t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 완전이진탐색트리 
    # root를 1로 한다
    # tree를 그릴 때, 0번은 쓰지 않는다
    tree = [0] * (n+1)


    print(f'{tc}')