# 안 보고 계속 풀기
# k 이동 가능 거리 -> 코드가 실행 가능한 조건
# => while k

T = int(input())
for tc in range(1, T+1):
    K, N, M = int(input().split())
    station = list(map(int, input().split()))

    count = 0  # 충전 횟수
    now = K    # 현재 위치 -> 처음 = 0 + 최대 이동 가능 거리
    charge = 0 # 마지막 충전 위치 -> 처음 = 0
