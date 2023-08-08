# flatten
import sys
sys.stdin = open('input (3).txt')

for tc in range(1, 11):
    dump = int(input())
    heights = list(map(int, input().split()))
    # 리스트 정렬 (오름차순)
    heights.sort()

    while dump: # 덤프가 가능한 동안 반복
        # 0번째 수(최소값)에 +1
        heights[0] += 1
        # -1번째 수(최댓값)에 -1
        heights[-1] -= 1
        # 다시 정렬
        heights.sort()
        # 덤프 횟수 차감
        dump -= 1
    # 최종적으로 가장 높은 값 - 가장 작은 값
    print(f'#{tc} {heights[-1] - heights[0]}')