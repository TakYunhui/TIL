T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 입력 받은 배열 오름차순 정렬로 변경
    numbers.sort()
    sorted_numbers = [0 for _ in range(N)]
    i = 0
    while numbers:
        # i가 0부터 짝수면
        if i % 2 == 0:
            # 가장 큰 수(마지막 인덱스 값) 넣기
            sorted_numbers[i] = max(numbers)
            # i 값은 증가
            i += 1
            # 넣었던 값 빼기
            numbers.pop(-1)
        elif i % 2 == 1:
            sorted_numbers[i] = min(numbers)
            i += 1
            numbers.pop(0)
    limited_list = sorted_numbers[:10]

    print(f'#{tc}',*limited_list)