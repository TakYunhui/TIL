# 달팽이
# 달팽이의 크기 = N

# delta를 사용해서 방향성 주기
# 칸이 끝날 때까지 이동
# 칸이 끝나면 방향 바꾸기
# 만약 이미 기존의 숫자가 들어가 있는 장소면
# 조건을 줘서 다른 방향으로 진행하게 만들기?
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)] # 2차원 배열 생성
    board[0][0] = 1 
    for i in range(N): # 모든 원소 arr[i]
        for j in range(N): # arr[i][j]
