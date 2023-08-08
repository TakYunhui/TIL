t = int(input())

for tc in range(1, t+1):
    result = 0
    pattern = input()
    N = len(pattern)
    target = input()
    M = len(target)

    count = 0
    p_idx = 0
    t_idx = 0
    while t_idx < M:
        if pattern[p_idx] != target[t_idx]:
            t_idx = t_idx - p_idx
            p_idx = -1
            count = 0
        t_idx += 1
        p_idx += 1

        if p_idx == N:
            result = 1
            break

    print(f'#{tc} {result}')