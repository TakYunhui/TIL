# 최대값과 최소값 위치의 차이
# 가장 큰 값과 작은 값의 index 찾기
# 가장 작은 수가 여러 개면 먼저 나오는 순서

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0 # 최소값의 인덱스, 가장 앞의 수로 가정
    max_idx = 0 # 최대값의 인덱스
    for i in range(1, N):
        if arr[min_idx] > arr[i]: # 같으면 이동 x
            min_idx = i
        if arr[max_idx] <= arr[i]: # 같으면 오른쪽을 택해야하므로 <=
            max_idx = i

    # abs(max_idx - min_idx)
    # max(max_idx, min_idx) - min(max_idx, min_idx)
    ans = max_idx - min_idx
    if ans < 0:
        ans = -ans
