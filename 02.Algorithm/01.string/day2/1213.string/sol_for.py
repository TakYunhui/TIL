import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    n = len(target)
    m = len(pattern)
    # 최종 결괏값
    result = 0  # 패턴이 문장에 몇 번 들어가는지 센다.
    p_idx = 0

    for t_idx in range(n - m + 1):
        if p_idx and t_idx + p_idx <= last_t_idx + m:
            continue
        for p_idx in range(m):
            # 패턴과 타겟이 동일하지 않은 경우가 한번이라도 나오면 조사 종료
            if pattern[p_idx] != target[t_idx + p_idx]:
                p_idx = 0
                break
        else: # for 문도 else가 있다 : break 된 적 없이 모두 순회했을 때,
            result += 1
            last_t_idx = t_idx
    print(result)