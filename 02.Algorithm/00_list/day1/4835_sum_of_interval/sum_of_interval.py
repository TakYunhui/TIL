import sys
sys.stdin = open('sample_input.txt')

# 모든 이웃한 수의 합 구하기
# 그 중 최대, 최소 값 구하기
# 그 둘의 차이 출력

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 최대 값이 들어갈 변수 max_v
    # 변수보다 값이 크면 해당 변수에 그 값을 넣어줄 것이기에
    # 0 지정
    max_v = 0
    # 최소 값이 들어갈 변수 min_v
    # 변수보다 값이 작으면 해당 변수에 그 값을 넣어줄 것이기에
    # 정수 a의 최대값 * M => 이러면 가장 큰 a 정수를 M개 더한 값과 같다
    min_v = 10000 * M
    # 우리가 봐야할 index 범위
    # 총 N개 중 M개씩의 합 묶음 계산
    # N - M + 1
    for i in range(N-M+1):
        result = 0
        # 이웃한 M개의 합 구하기
        # result = numbers[i] + numbers[i+1] + numbers[i+2]
        # 위 식은 M이 3개 일때만 정상 작동
        # 모든 변수에서 알맞은 값이 나오려면...
        # M범위 내에서
        for j in range(M):
            # i = 0 | j = 0, 1, 2
            # i = 1 | j = 1, 2, 3
            # i 값이 변함에 따라 j도 변하게
            # 인덱스를 i+j 로 잡아준다
            result += numbers[i + j]
        # for 문 안에 if 조건문을 넣으면
        # for 문 누적합이 다 완료되지 않은 과정의 값이 들어가므로
        # for 문 바깥에서 이웃한 범위의 합이 완료된 result를 가지고
        # max_v, min_v와 비교해 최대, 최소 값을 구해준다
        if result > max_v:
            max_v = result
        if result < min_v:
            min_v = result
    print(f'#{tc} {max_v - min_v}')








