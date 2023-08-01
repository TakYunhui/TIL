# 조망권
# 자기 인덱스 +- 2 범위에 자기보다 작은 게 2개면 조망권 확보!
# => 지정 범위에 자기와 같거나 큰 수가 하나라도 있으면 확보 X
# 조건을 둔다면
# 1. 작은 수 2개 있는지 COUNT or 2. 큰 수 하나라도 있는지?
# 반복문으로 전체 범위 순회하면서
# 조건 확인 후, 조망권을 얻는 건물 찾고 하나 찾을 때마다 COUNT


# 조건
# 4 <= N <= 1000
# 0 <= 리스트 안의 요소 값 <= 255
# 순회할 범위 리스트를 [0, 0, list[i], ... , list[N], 0, 0] 에서
# 자기 주변 +- 2범위 내 숫자를 확인해서
# 모두 자신보다 작다면 그 중 가장 큰 수를 본인에서 뺀다
# 그 수를 저장하고 합을 구한다

T = 10
for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    view = 0
    # 맨 왼쪽, 오른쪽 두 칸은 0 0 이므로 2부터 N-2까지 범위 지정
    for i in range(2, N-2):
        # 비교할 값을 [0]부터 본다 -> 기준을 잡는다
        max_h = heights[i - 2]
        # -1의 범위 비교 
        if max_h < heights[i-1]:
            max_h = heights[i-1]
        # +1의 범위 비교
        if max_h < heights[i+1]:
            max_h = heights[i+1]
        # +2의 범위 비교
        if max_h < heights[i+2]:
            max_h = heights[i+2]
        # -2는 0이고, range는 2부터 시작하므로 비교 필요 x
        # 1번 인덱스는 -1부터 보기 때문...
        
        # max_h에는 비교한 값 중 가장 큰 수가 들어가게 된다
        # 이 값이 현재 보고 있는 i번째 건물의 높이보다 작다면
        # 현재 건물의 높이 - 가장 큰 수 = 조망권이 보장된 건물의 수
        if heights[i] > max_h:
            view += heights[i] - max_h
    print(f'#{tc} {view}')



# for 문 만들기
