# KMP 알고리즘
import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

# 패턴 내에 패턴이 존재하는지,
# 그 정보를 담기 위한 리스트 만드는 함수
def make_lps(pattern):
    # 중개 리스트
    lps = [0] * len(pattern)
    # 중개 리스트의 각 인덱스에
    # 이전 패턴 정보 누적 값을 담기 위한 인덱스 정의
    lps_idx = 0
    # 가장 첫 칸[0]은 똑같은 패턴이 있을 수 없으니까
    for i in range(1, len(pattern)):
        # 이전번 글자와 지금 조사하는 글자가 같다면
        if pattern[i] == pattern[lps_idx]:
            lps[i] = lps_idx + 1
            lps_idx += 1
        else:
            # 다를 때는 lps_idx를 0으로 초기화 시켜서
            # 패턴의 0번째와 '다시 비교'
            lps_idx = 0
            if pattern[i] == pattern[lps_idx]:
                lps[i] = lps_idx + 1
                lps_idx += 1
    return lps


# 그렇게 만들어진 lps를 활용해서
# KMP 탐색
def KMP(pattern, target):
    lps = make_lps(pattern)

    # 조사 시작 자체는 brute force랑 똑같이
    p_idx = 0
    t_idx = 0
    result = 0
    while t_idx < len(target):
        if pattern[p_idx] == target[t_idx]:
            p_idx += 1
            t_idx += 1
        else:
            if p_idx == 0:
                t_idx += 1
            else:
                p_idx = lps[p_idx - 1]
        # 패턴 끝까지 다 찾았으면 reuslt + 1 증가
        if p_idx == len(pattern):
            result += 1
            p_idx = 0

    return


for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    print(make_lps(pattern))