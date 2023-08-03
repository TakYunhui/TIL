# swea 소인수분해
# N = 2^a * 3^b * 5^c * 7^d * 11^e
# a, b, c, d, e => 각 숫자로 나눠진 횟수?
# N을 소인수로 나눈 몫이 0이 될 때까지 나누기를 반복
# 나눌 때마다 횟수 count해 각 변수에 넣기

T = int(input())
for tc in range(1, T+1):
    # 각 tc 별 숫자 N 입력
    N = int(input())

