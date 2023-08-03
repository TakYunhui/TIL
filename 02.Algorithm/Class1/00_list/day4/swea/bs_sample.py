T = int(input())

# 테스트 케이스 별로
# P: 전체 책의 쪽수 -> 탐색할 범위
# A, B: 각각 이진탐색을 사용해 찾을 쪽 번호(target)
# 탐색 횟수 count가 더 적은 쪽이 승리(출력)
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    # P까지의 범위를 갖는 배열 생성
    arr = list(range(1, P+1))
    A_count = 0
    B_count = 0

    # A_count 구하기
    start = 0
    end = P-1
    while start < end:
        mid = int((start+end)/2)
        if arr[mid] == A:
            break
        elif arr[mid] > A:
            end = mid - 1
            A_count += 1
        else:
            start = mid + 1
            A_count += 1
    # B_count 구하기
    start = 0
    end = P-1
    while start < end:
        mid = int((start+end)/2)
        if arr[mid] == B:
            break
        elif arr[mid] > B:
            end = mid - 1
            B_count += 1
        else:
            start = mid + 1
            B_count += 1
    # 탐색 횟수 비교
    if A_count > B_count:
        result = 'B'
    elif A_count < B_count:
        result = 'A'
    else:
        result = '0'
    print(f'#{tc} {result}')