import sys
# 파일 open
sys.stdin = open('sample_input.txt')

T = int(input())
for num in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0
    # 문제에서 주어진 범위 중 가장 큰 값을 넣어도 됨
    max_num = numbers[0]
    min_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
        elif number < min_num:
            min_num = number
    result = max_num - min_num
    print(f'#{num} {result}')


