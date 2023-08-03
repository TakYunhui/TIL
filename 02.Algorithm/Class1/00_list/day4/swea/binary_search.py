# 이진탐색
# A, B에게 찾을 쪽 번호를 알려줌
# -> 이진탐색으로 먼저 찾는 사람이 이김

T = int(input())

# 테스트 케이스 별로
# P: 전체 책의 쪽수 -> 탐색할 범위
# A, B: 각각 이진탐색을 사용해 찾을 쪽 번호(target)
# 탐색 횟수 count가 더 적은 쪽이 승리(출력)
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    A_count = 0
    B_count = 0

    # 배열 사용 x -> 인덱스 접근 x, 숫자 순서대로 접근
    # A_count 구하기

    start = 1 # 1페이지
    end = P   # 마지막 페이지
    while True:
        mid = int((start+end)/2) # 중간 페이지
        A_count += 1             # 첫번째 탐색
        if mid == A: # 중간값이 찾는 타겟이면 반복문 종료 
            break
        # 이후 탐색시 마다 count 증가
        # 중간값이 타겟보다 크면 오른쪽 안 봐도 됨
        # 다음 탐색의 end = mid (인덱스 접근이 아니므로 + - 1이 필요없음_
        elif mid > A:
            end = mid
            A_count += 1
        # 중간값이 타겟보다 작으면 왼쪽 안 봐도 됨
        # 다음 탐색의 start = mid
        else:
            start = mid
            A_count += 1
    # B_count 구하기
    start = 1
    end = P
    while True:
        mid = int((start+end)/2)
        B_count += 1
        if mid == B:
            break
        elif mid > B:
            end = mid
            B_count += 1
        else:
            start = mid
            B_count += 1
    # 탐색 횟수 비교
    if A_count > B_count:
        result = 'B'
    elif A_count < B_count:
        result = 'A'
    else:
        result = '0'
    print(f'#{tc} {result}')