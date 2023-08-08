# 내가 찾고자 하는 pattern 이 target 안에 있냐/없냐
# + 몇 개나 있는지 찾기
# t_idx 와 p_idx 같이 조절하며 찾기
# 고지식한 알고리즘
import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    # 조사 대상 두개 (pattern, target)의 index를 담을 변수 선언
    p_idx = 0
    t_idx = 0
    # 최종 결괏값
    result = 0  # 패턴이 문장에 몇 번 들어가는지 센다.
    # 조사를 언제까지 반복?
    # 타겟의 끝까지 조사하면서 pattern이 몇번 나오는지 세야한다
    len_target = len(target) # 길이를 변수에 선언해주면 조사할 때마다 len()함수로 확인하는 과정 안 가져도 됨
    while t_idx < len_target:
        # t_idx 번째의 값과 p_idx 번째의 값이
        # 같거나 틀릴 때 취해야 할 행동
        if target[t_idx] != pattern[p_idx]:
            t_idx = t_idx - p_idx
            p_idx = -1
        # 같거나 틀린 상황 이외에
        # 모든 상황에 대해서
        # p_idx 와 t_idx는 증가할 것
        p_idx += 1
        t_idx += 1
        
        if p_idx == len(pattern):
            result += 1 # 패턴 한번 찾았다
            p_idx = 0   # 다음부터는 다시 0번부터 조사
    print(f'#{tc} {result}')