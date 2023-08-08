# S/W 2일차 - Sum
# 100 x 100 2차원 배열
# 행의 합, 열의 합, 대각선의 합 중 최댓값
# 1. 행/열의 합 중 최댓값 구하기
# 2. 대각선의 합 2개 중 최댓값 구하기
import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(10):
    tc = int(input())
    # 2차원 배열 선언
    # 100개의 행, 100개의 열
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행의 합 중 최댓값 구하기
    # 이중 for문으로 한 행씩 합을 다 구하며 비교
    # 최대 값을 저장할 변수는 반복문 밖으로 빼둠( 반복문 실행시 초기화 x)
    max_row = 0
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
        if row_sum > max_row:
            max_row = row_sum
    # 열의 합 중 최댓값 구하기 (위와 방식 같음)
    max_col = 0
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += arr[j][i]
        if col_sum > max_col:
            max_col = col_sum

    # 대각선의 합 중 최댓값 구하기
    # 단일 for문 이용 -> 대각선 합 1, 2의 변수를 반복문 밖으로
    max_diagnol = 0
    diagnol1 = 0
    diagnol2 = 0
    for i in range(100):
        diagnol1 += arr[i][i]
        diagnol2 += arr[i][99 - i]
        if diagnol1 >= diagnol2:
            max_diagnol = diagnol1
        else:
            max_diagnol = diagnol2

    # 총 4가지 값(행, 열, 대각선1, 대각선2) 중 최댓값 구하기
    max_value = max([max_row, max_col, max_diagnol])
    print(f'#{tc} {max_value}')






