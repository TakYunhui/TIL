# 가장 큰 수, 가장 작은 수, 두번째로 큰 수, 두번째로 작은 수

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 입력 받은 배열 오름차순 정렬로 변경
    numbers.sort()
    # 새로 값을 넣어줄 배열 생성 
    sorted_numbers = [0 for _ in range(N)]
    i = 0
    # numbers 값이 있는 동안 
    while numbers:
        # i(인덱스)가 짝수면
        if i % 2 == 0:
            # 가장 큰 수(마지막 인덱스 값) 넣기
            sorted_numbers[i] = max(numbers)
            # i 값은 증가
            i += 1
            numbers.pop(-1)
        elif i % 2 == 1:
            sorted_numbers[i] = min(numbers)
            i += 1
            numbers.pop(0)

    # 10개까지만 출력 조건
    limited_list = sorted_numbers[:10]

    print(f'#{tc}', *limited_list)
