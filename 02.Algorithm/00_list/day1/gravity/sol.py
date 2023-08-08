# 90도 회전 -> 리스트에서 오른쪽으로 이동
# 낙차를 리턴: 낙차?
# 방의 가로 & 세로 길이는 항상 100
# 범위 0 ~ 100
import sys
sys.stdin = open('input.txt')

# 전체 테스트 케이스 수
# input 함수는 입력 받은 값을 항상 문자열로 반환
T = int(input())

# T 번 만큼 순회하면서 각 tc에 대한 문제 해결
# ctrl + shift + F10 -> 코드 실행

for tc in range(1, T+1):
    # 상자들이 담겨있는 칸의 개수
    N = int(input())
    # 각 상자들의 높이가 담겨 있는 값을 받는다.
    # 공백을 기준으로 나눠서 입력 받은 문자열들
    # 비교하기 쉽게 int로 바꾸서 list에 담는다
    boxes = list(map(int, input().split()))
    # 최종 결괎값
    result = 0
    # 모든 상황에 대한 낙차 값을 구하기 위해 전체 순회
    for i in range(N): # N = 9 | i 에는 0 ~ 8
        # i 번째 상자가 떨어질 수 있는 최대
        # 방해 받지 않고 떨어지는 최대
        # 전체 길이 - 내 위치 + 1
        # +1 해줘야 내 위치는 빼고 계산
        max_H = N - (i+1)
        # 내 다음에 오는 상자들 중에
        # 나보다 크거나 같은 값들 찾기
        # i = 0 | 0 + 1 ~ N - 1
        # i = 1 | 2 + 1 ~ N - 1
        for j in range(i+1, N):
            # 내 높이보다 j 번째 위치가 크거나 같은 값 찾기
            if boxes[i] <= boxes[j]:
                max_H -= 1
        # print(max_H)
        # i 번째 값이 최대로 떨어질 수 있는 낙차 값이
        # 현재 기록해둔 최종 결괏값보다 크다면,
        if result < max_H:
            result = max_H
    print(f'#{tc} {result}')